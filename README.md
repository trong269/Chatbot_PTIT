# Chatbot_PTIT

- Cách chạy server:
+ Tải các thư viện trong requirements.txt
+ Tải postgres, chỉnh sửa thông tin của database cá nhân trong file backend/chatbot_service/api/.env
+ Chạy terminal trong folder chatbot_service -> nhập lệnh uvicorn api.app.main:app --reload
+ Test các api trong postman