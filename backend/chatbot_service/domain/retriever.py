import uuid
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain_chroma import Chroma
from langchain.storage import InMemoryByteStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.load import dumps, loads
from langchain_core.documents.base import Document
from domain.api_key import API_KEY, GEMINI_MODEL, EMBEDDING_MODEL


# Tạo lớp loader tùy chỉnh với encoding 'utf-8'
class UTF8TextLoader(TextLoader):
    def __init__(self, file_path):
        super().__init__(file_path, encoding='utf-8')

# tạo lớp retriever custom
class Retriever(MultiVectorRetriever):
    def __init__(self, api_key , embedding_model ):
        super().__init__(
            vectorstore= Chroma(
                collection_name="documents", 
                embedding_function= GoogleGenerativeAIEmbeddings(
                    model=embedding_model,
                    google_api_key= api_key)),
            byte_store= InMemoryByteStore(), 
            id_key="doc_id"
        )


    def documents_loader(self, folder_path) -> list[Document]:
        """ load dữ liệu từ thư mục"""
        documents = DirectoryLoader(folder_path, glob="*.txt", loader_cls=UTF8TextLoader).load()
        return documents

    def split_documents( self , documents, chunk_size: int, chunk_overlap: int ) -> (list[Document], list[str]):
        """ chia nhỏ văn bản thành các phần nhỏ"""
        # khai báo text_splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size= chunk_size,
            chunk_overlap= chunk_overlap,
            separators=["\n\n", "\n", "."],
            length_function = len
        )
        # tạo id cho từng văn bản
        doc_ids = [str(uuid.uuid4()) for _ in documents]
        chunks = []
        for i in range(len(documents)):
            chunked_doc = text_splitter.split_documents([documents[i]])
            for chunk in chunked_doc:
                chunk.metadata[self.id_key] = doc_ids[i]
            chunks.extend(chunked_doc)
        return (chunks, doc_ids)
    
    def make_batch_chunks(self, chunks: list[Document], max_batch_size: int) -> list[list[Document] ]:
        """ tạo batch cho việc thêm tài liệu vào retriever"""
        for i in range(0, len(chunks) , max_batch_size):
            if( i + max_batch_size < len(chunks)):
                yield chunks[i:i+max_batch_size]
            else: yield chunks[i : (len(chunks))]

    # hàm thêm tài liệu vào retriever
    def add_documents_to_retriever(self, data_path: str, chunk_size: int = 300, chunk_overlap: int = 50, max_batch_size: int = 166)-> None:
        """ thêm tài liệu vào retriever"""
        documents = self.documents_loader(data_path)
        chunks , doc_ids = self.split_documents(documents, chunk_size, chunk_overlap)
        batches = self.make_batch_chunks(chunks, max_batch_size)
        # thêm từng batch một vào vectorstore
        for batch in batches:
            self.vectorstore.add_documents(batch)
        # thêm tài liệu gốc vào docstore
        self.docstore.mset(list(zip(doc_ids, documents)))
    
    def multi_query(self, queries: list[str], top_k: int) -> list[Document]:
        """ thực hiện nhiều truy vấn và xếp hạng lại các tài liệu được trả về"""
        retrieved_results = self.map().invoke(queries)
        re_ranked_doccuments = self.re_ranking(retrieved_results, top_k)
        return re_ranked_doccuments

    def re_ranking(self, results: list[ list ], top_k: int, k : int = 60)-> list[Document]:
        """ xếp hạng lại các tài liệu được trả về từ retriever"""
        scores = {}
        for docs in results:
            for rank , doc in enumerate(docs):
                doc_str = dumps(doc)
                if doc_str not in scores.keys():
                    scores[doc_str] = 0
                scores[doc_str] += 1/(rank+k)
        rerank_results = [
            loads(doc_str) for doc_str, score in sorted(scores.items(), key=lambda item: item[1], reverse=True)
        ]
        if top_k <= len(rerank_results):
            return rerank_results[:top_k]
        return rerank_results
