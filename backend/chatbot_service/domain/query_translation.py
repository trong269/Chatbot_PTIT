from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from domain.api_key import API_KEY, GEMINI_MODEL, EMBEDDING_MODEL


class QueryTranslation:
    def __init__(self, api_key=API_KEY, model=GEMINI_MODEL):
        self.llm = ChatGoogleGenerativeAI( model=model, api_key=api_key, temperature=0.3)

    def multi_query(self, question : str, k : int = 2)-> list[str]:
        """ Tạo ra nhiều câu hỏi khác nhau từ câu hỏi đầu vào"""
        template = """Bạn là chuyên gia tư vấn thông tin về Học Viện Công Nghệ Bưu Chính Viễn Thông. 
        Nhiệm vụ của bạn là tạo ra {k} phiên bản khác nhau của câu hỏi mà người dùng đưa ra để truy xuất các tài liệu liên quan từ cơ sở dữ liệu vector. 
        Bằng cách tạo ra nhiều góc nhìn khác nhau về câu hỏi của người dùng, mục tiêu của bạn là giúp người dùng vượt qua một số hạn chế của phương pháp tìm kiếm tương tự dựa trên khoảng cách. 
        Hãy cung cấp các câu hỏi thay thế này, chỉ in ra dòng chứa các câu hỏi không in dòng thừa hoặc dòng không liên quan, mỗi câu hỏi trên một dòng . 
        Câu hỏi gốc: {question}
        """
        prompt_template = ChatPromptTemplate.from_template(template) 
        chain = prompt_template | self.llm | StrOutputParser() | (lambda x: x.split("\n"))
        queries = chain.invoke({"question": question, "k" : k })
        return [query for query in queries if query != "" and query != " "]

    def decomposition(self, question: str, k: int = 3)-> list[str]:
        """ Phân rã câu hỏi đầu vào thành các câu hỏi con"""
        template = """
            Bạn là một trợ lý hữu ích tạo ra nhiều câu hỏi con liên quan đến một câu hỏi đầu vào.
            Mục tiêu là phân chia câu hỏi đầu vào thành một tập hợp các vấn đề/câu hỏi nhỏ hơn có thể được trả lời riêng biệt.
            Hãy tạo ra nhiều truy vấn tìm kiếm liên quan đến: {question}
            chỉ in ra các câu hỏi, không in ra dòng trống hoặc dòng không liên quan.
            Kết quả đưa ra {k} truy vấn mới:
            """
        prompt_template = ChatPromptTemplate.from_template(template) 
        chain = prompt_template | self.llm | StrOutputParser() | (lambda x: x.split("\n"))
        queries = chain.invoke({"question": question, "k" : k })
        return [query for query in queries if query != "" and query != " "]
    def HyDE(self , question: str) -> str:
        """đưa ra câu trả lời giả định cho câu hỏi đầu vào"""
        template = """Bạn là chuyên gia tư vấn thông tin về Học Viện Công Nghệ Bưu Chính Viễn Thông,
            giả sử bạn đã biết thông tin có trong câu hỏi, hãy viết một đoạn văn ngắn giả định số liệu liệu không cần chính xác 
            nhưng ngữ nghĩa phải giống với câu trả lời thực tế nhất
            để trả lời câu hỏi
            Câu hỏi: {question}
            chỉ in ra các câu trả lời, không in ra dòng trống hoặc dòng không liên quan.
            Đoạn văn:
            """
        prompt_template = ChatPromptTemplate.from_template(template)
        chain = prompt_template | self.llm | StrOutputParser()
        return chain.invoke({"question": question} )

# QT = QueryTranslation()
# queries = QT.multi_query("Chương trình tuyển sinh của Học viện năm 2024 và chỉ tiêu tuyển sinh của trường")
# print(queries)
# print(len(queries))
# for query in queries:
#     print(QT.HyDE(query))
#     print("")