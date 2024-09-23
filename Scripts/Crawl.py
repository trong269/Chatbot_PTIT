import requests
from bs4 import BeautifulSoup
import os 

DATA_FOLDER_PATH = 'Data\Raw data'

def crawl_lich_su_truyen_thong():
    # URL của trang cần crawl
    url = 'https://ptit.edu.vn/gioi-thieu/tong-quan-hoc-vien/lich-su-truyen-thong'

    # Gửi yêu cầu đến trang web
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="elementor elementor-27825")

        # Tìm tất cả các đoạn văn (p) trong nội dung
        content_paragraphs = body.find_all(['p', 'h2'])

        # tìm bảng
        table_data = []
        table = body.find('table', class_="")
        rows = table.find_all('tr')
        for row_id, row in enumerate(rows):
            columns = row.find_all('td')
            if columns:
                ngay = columns[0].text.strip()
                noi_dung = columns[1].text.strip()
                table_data.append(f"Ngay: {ngay}\n{noi_dung}")

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        content += "\n".join(table_data)
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'lich_su_truyen_thong.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')


def crawl_nguon_nhan_luc():
    url = 'https://ptit.edu.vn/gioi-thieu/nguon-nhan-luc'
    # Gui y/c den trang web
    response = requests.get(url)
    # Kiem tra xem y/c co thanh cong khong
    if response.status_code == 200:
        # Phan tich HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tieu de
        title = soup.title.string
        # Truy cap vao body
        body = soup.find('div', class_ = 'e-con-inner')
        content_body = body.find_all(['span'])
        # Ket hop noi dung vao chuoi
        content = "\n".join([p.get_text() for p in content_body]) # Xuong dong o moi lan het 1 doan van ban
        # Luu du lieu vao data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'nguon_nhan_luc.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Loi: Khong the truy cap trang. Ma trang thai: {response.status_code}')    

def crawl_co_so_vat_chat():
    url = 'https://ptit.edu.vn/gioi-thieu/co-so-vat-chat'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        body = soup.find('div', class_='e-con-inner')
        content_body = body.find_all(['p'])
        content = "\n".join(p.get_text() for p in content_body)
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'co_so_vat_chat.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Loi: Khong the truy cap trang. Ma trang thai:{response.status_code}')



if __name__ == '__main__':
    crawl_lich_su_truyen_thong()
    crawl_nguon_nhan_luc()
    crawl_co_so_vat_chat()