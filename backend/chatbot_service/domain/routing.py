from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from domain.config import API_KEY, GEMINI_MODEL, TEMPERATURE
from pydantic import BaseModel, Field
from typing import Literal

class RouteQuery(BaseModel):
    """
    RouteQuery: Lớp này chứa thông tin cần thiết để chọn nguồn dữ liệu phù hợp để trả lời câu hỏi của người dùng
    """
    # sử dụng Literal để chọn 1 ptu trong mảng
    datasources: Literal["thong_tin_gioi_thieu", "tin_tuc_va_su_kien", "cac_chuong_trinh_dao_tao_cu_the", "khong_lien_quan"] = Field(
        ...,description="Với câu hỏi của người dùng, hãy chọn nguồn dữ liệu nào có liên quan nhất để trả lời câu hỏi của họ"
        )


class Router():
    def __init__(self , api_key: str , model:str , RouteQuery: RouteQuery):
        self.llm = ChatGoogleGenerativeAI( api_key = api_key, model= model , temperature=TEMPERATURE).with_structured_output(RouteQuery)
    def routing(self, query: str) -> str:
        system = """
            Bạn là chuyên gia định tuyến câu hỏi của người dùng đến nguồn dữ liệu phù hợp. Dưới đây là danh sách các nguồn dữ liệu:
            1. 'Thông tin giới thiệu': Chứa các thông tin chung về học viện như lịch sử, sứ mệnh, cơ sở vật chất, cơ cấu tổ chức, các khoa, các ngành học, các câu lạc bộ, đội ngũ giảng viên...
            2. 'Tin tức và sự kiện': Cập nhật các sự kiện mới nhất, các hoạt động, hội thảo diễn ra tại học viện.
            3. 'Các chương trình đào tạo cụ thể': Cung cấp thông tin chi tiết về các từng chương trình đào tạo mà học viện đang cung cấp
            4. "Thông tin không liên quan": Câu hỏi không liên quan đến các nguồn dữ liệu trên
            Dựa trên câu hỏi của người dùng, hãy chọn nguồn dữ liệu phù hợp nhất, nếu không có thì chọn không liên quan.
        """
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system),
                ("human", "{query}"),
            ]
        )
        router = prompt | self.llm
        result = router.invoke({"query": query})
        if result: return result.datasources
        return "khong_lien_quan"

# router = Router(API_KEY, GEMINI_MODEL, RouteQuery)
# data = router.routing("Học viện có bao nhiêu chương trình khoa ?")
# print(data)
