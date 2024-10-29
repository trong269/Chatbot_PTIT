from domain.retriever import Retriever
from domain.query_translation import QueryTranslation
from domain.routing import Router, RouteQuery
from domain.api_key import API_KEY, GEMINI_MODEL, EMBEDDING_MODEL, TEMPERATURE
# from .api_key import API_KEY, GEMINI_MODEL, EMBEDDING_MODEL
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents.base import Document
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

CHUNK_SIZE = 300
OVERLAP_SIZE = 50
MAX_BATCH_SIZE = 166
DATA_PATH1 = "C:\workspace\AI\Chatbot_PTIT\Data\Gioi thieu"
DATA_PATH2 = "C:\workspace\AI\Chatbot_PTIT\Data\Chuong trinh dao tao"
DATA_PATH3 = "C:\workspace\AI\Chatbot_PTIT\Data\Other"
DATABASEPATH1 = "C:\workspace\AI\Chatbot_PTIT\Data\ChromaDB_1"
DATABASEPATH2 = "C:\workspace\AI\Chatbot_PTIT\Data\ChromaDB_2"
DATABASEPATH3 = "C:\workspace\AI\Chatbot_PTIT\Data\ChromaDB_3"
# print(API_KEY)

class ChatBot():
    def __init__(self , api_key: str = API_KEY , model: str = GEMINI_MODEL, embedding_model: str = EMBEDDING_MODEL, top_k: int = 5 ):
        self.api_key = api_key 
        self.top_k = top_k
        self.router = Router(api_key = self.api_key , model = model, RouteQuery = RouteQuery)

        self.retriever1 = Retriever(api_key = self.api_key, embedding_model = embedding_model, persist_directory=DATABASEPATH1)
        self.retriever1.add_documents_to_retriever(data_path=DATA_PATH1, chunk_size = CHUNK_SIZE, chunk_overlap = OVERLAP_SIZE, max_batch_size = MAX_BATCH_SIZE)

        self.retriever2 = Retriever(api_key = self.api_key, embedding_model = embedding_model, persist_directory=DATABASEPATH2)
        self.retriever2.add_documents_to_retriever(data_path= DATA_PATH2, chunk_size = CHUNK_SIZE, chunk_overlap = OVERLAP_SIZE, max_batch_size = MAX_BATCH_SIZE)

        self.retriever3 = Retriever(api_key = self.api_key, embedding_model = embedding_model, persist_directory=DATABASEPATH3)
        self.retriever3.add_documents_to_retriever(data_path= DATA_PATH3, chunk_size = CHUNK_SIZE, chunk_overlap = OVERLAP_SIZE, max_batch_size = MAX_BATCH_SIZE)

        self.query_translation = QueryTranslation(api_key = self.api_key, model = model)
        self.llm = ChatGoogleGenerativeAI( model = model, api_key = self.api_key, temperature= TEMPERATURE)

    def chat(self, question: str, history_messages: list[str] )-> str:
        """ Hàm chính của chatbot"""
        # chuyển câu hỏi thành các truy vấn
        queries = self.translate_query(question, k_query= 6 )
        # phân loại các truy vấn vào các nguồn dữ liệu
        routing = self.routing_document(queries)
        # tìm kiếm các tài liệu phù hợp
        documents = self.retrival(routing, queries)
        history_messages_text = "\n".join(history_messages) if len(history_messages) <= 10 else "\n".join(history_messages[-10 :])
        with open("C:\workspace\AI\Chatbot_PTIT\memory.txt", 'w' , encoding='utf-8') as f:
            f.write(history_messages_text)
        print("--------------------------")
        for docs , queries in routing.items():
            print(f"có {len(queries)} thuộc về {docs}")
        print(f"tìm được {len(documents)} tài liệu")
        print("--------------------------")
        print()
        template = """Bạn là một chuyên gia tư vấn của Học Viện Công Nghệ Bưu Chính Viễn Thông hỗ trợ trả lời các câu hỏi của người dùng. Hãy sử dụng kiến thức của bạn cùng với ký ức của bạn trong quá khứ để đưa ra câu trả lời chính xác và đầy đủ nhất cho câu hỏi mới của người dùng. Nếu thông tin không nằm trong kiến thức hoặc ký ức của bạn, hãy nói rằng bạn không biết thông tin đó và hướng dẫn người dùng tìm kiếm thông tin nơi khác. Dưới đây là kiến thức mà bạn biết, ký ức của bạn đã trao đổi cùng người dùng trong quá khứ và câu hỏi mới:"
            kiến thức của bạn: {context}

            ký ức của bạn: {history}
            
            Câu hỏi mới của người dùng: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm | StrOutputParser()
        anwser = chain.invoke({"question": question, "context": documents, "history": history_messages_text})
        return anwser
    def translate_query(self, query:str , k_query : int )->list[str]:
        """ tạo ra nhiều truy vấn ở nhiều khía cạnh khác nhau từ câu hỏi đầu vào"""
        k_query = k_query - 2
        queries = [query]
        multi_queries = self.query_translation.multi_query(query, k = k_query // 2)
        decomposition_queries = self.query_translation.decomposition(query, k = k_query - (k_query // 2))
        HyDE_query = self.query_translation.HyDE(query)
        queries.extend(multi_queries)
        queries.extend(decomposition_queries)
        queries.append(HyDE_query)
        if len(queries) > k_query:
            return queries[:k_query]
        return queries

    def routing_document(self , queries:list[str]) -> dict[str, list[str]]:
        """ Phân loại các câu hỏi vào các nguồn dữ liệu phù hợp"""
        datasources = [self.router.routing(query) for query in queries]
        results = dict({
            "retriever1": [],
            "retriever2": [],
            "retriever3": [],
            "khong_lien_quan": []
        })
        for i in range(len(datasources)):
            if datasources[i] == "thong_tin_gioi_thieu":
                results["retriever1"].append(queries[i])
            elif datasources[i] == "cac_chuong_trinh_dao_tao_cu_the":
                results["retriever2"].append(queries[i])
            elif datasources[i] == "tin_tuc_va_su_kien":
                results["retriever3"].append(queries[i])
            else:
                results["khong_lien_quan"].append(queries[i])
        return results

    def retrival(self, routing: dict, queries: list[ str ] )-> list[Document]:
        """ Tìm kiếm các tài liệu phù hợp với các câu hỏi"""
        results = []
        len_prev = 0
        for key, value in routing.items():
            if key == "retriever1" and len(value) > 0:
                results.extend( self.retriever1.multi_query(value, top_k = self.top_k))
                print(f"tìm được {len(results)} tài liệu từ thông tin giới thiệu về học viện")
                len_prev = len(results)
            elif key == "retriever2" and len(value) > 0:
                results.extend( self.retriever2.multi_query(value, top_k = self.top_k))
                print(f"tìm được {len(results) - len_prev} tài liệu từ chương trình đào tạo của học viện")
                len_prev = len(results)
            elif key == "retriever3" and len(value) > 0:
                results.extend( self.retriever3.multi_query(value, top_k = self.top_k))
                print(f"tìm được {len(results) - len_prev} tài liệu từ tin tức và sự kiện của học viện")
                len_prev = len(results)
            else:
                continue
            with open("C:\workspace\AI\Chatbot_PTIT\log2.txt", 'w' , encoding='utf-8') as f:
                text = results
                text = "\n---------------------------\n".join([ doc.page_content for doc in text ])
                f.write(text)
        return results

# questions = "ptit có bao nhiêu câu lạc bộ ?"

# chatbot = ChatBot( api_key= API_KEY, model= GEMINI_MODEL, embedding_model= EMBEDDING_MODEL, top_k = 5)

# anwser = chatbot.chat(questions)
# print(anwser)
