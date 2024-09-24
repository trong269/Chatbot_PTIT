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

def crawl_y_nghia_logo():
    url = 'https://ptit.edu.vn/gioi-thieu/tong-quan-hoc-vien/y-nghia-logo-hoc-vien'
    response = requests.get(url)
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="elementor-element elementor-element-378168e elementor-widget elementor-widget-text-editor")

        content_paragraphs = body.find_all(['div'])

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'y_nghia_logo.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_tam_nhin_su_mang():
    url = 'https://ptit.edu.vn/gioi-thieu/tong-quan-hoc-vien/tam-nhin-su-mang'
    response = requests.get(url)
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="elementor-element elementor-element-9c44e2e elementor-widget elementor-widget-text-editor")

        content_paragraphs = body.find_all(['div'])

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'tam_nhin_su_mang.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_triet_ly_giao_duc():
    url = 'https://ptit.edu.vn/gioi-thieu/tong-quan-hoc-vien/triet-ly-giao-duc'
    response = requests.get(url)
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="e-con-inner")
        content_paragraphs = body.find_all(['h2', 'p'])

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'triet_ly_giao_duc.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_chien_luoc_phat_trien():
    url = 'https://ptit.edu.vn/gioi-thieu/tong-quan-hoc-vien/chien-luoc-phat-trien-giai-doan-2021-2025-tam-nhin-2030'
    response = requests.get(url)
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="e-con-inner")
        content_paragraphs = body.find_all(['h2', 'h4', 'p'])

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'chien_luoc_phat_trien.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_dang_uy_hoc_vien():
    # URL của trang cần crawl
    url = 'https://ptit.edu.vn/gioi-thieu/co-cau-to-chuc/dang-uy-hoc-vien'

    # Gửi yêu cầu đến trang web
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="the_content_wrapper")

        content_paragraphs = body.find_all(['h5'])
        # tìm bảng
        table_data = []
        table = body.find('table', id="tblNoidung")
        rows = table.find_all('tr')
        for row_id, row in enumerate(rows):
            columns = row.find_all('td')
            if columns:
                name = columns[1].text.strip()
                position = columns[2].text.strip()
                table_data.append(f"{name} là {position}")

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        content += "\n".join(table_data)
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'dang_uy_hoc_vien.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_hoi_dong_hoc_vien():
    # URL của trang cần crawl
    url = 'https://ptit.edu.vn/gioi-thieu/co-cau-to-chuc/hoi-dong-hoc-vien'

    # Gửi yêu cầu đến trang web
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="the_content_wrapper")

        title_1 = body.find_all(['h4'])
        # tìm bảng
        table_data = []
        table = body.find('table', class_="")
        rows = table.find_all('tr')
        for row_id, row in enumerate(rows):
            columns = row.find_all('td')
            if columns:
                name = columns[1].text.strip()
                position = columns[2].text.strip()
                table_data.append(f"{name}, {position}")
        # tìm text
        content_paragraphs = body.find_all(['p'])
        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in title_1]) + "\n\n"
        content += "\n".join(table_data) + "\n\n"
        content += "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'hoi_dong_hoc_vien.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_ban_giam_doc_hoc_vien():
    url = 'https://ptit.edu.vn/gioi-thieu/co-cau-to-chuc/ban-giam-doc-hoc-vien'
    response = requests.get(url)
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="e-con-inner")
        content_paragraphs = body.find_all(['h1', 'h2', 'p'])

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join([p.get_text() for p in content_paragraphs])
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'ban_giam_doc_hoc_vien.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_hoi_dong_khoa_hoc_va_dao_tao():
    # URL của trang cần crawl
    url = 'https://ptit.edu.vn/gioi-thieu/co-cau-to-chuc/hoi-dong-khoa-hoc-va-dao-tao'

    # Gửi yêu cầu đến trang web
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="the_content_wrapper")

        # tìm bảng
        table_data = []
        table = body.find('table', class_="")
        rows = table.find_all('tr')
        for row_id, row in enumerate(rows):
            columns = row.find_all('td')
            if columns:
                name = columns[1].text.strip()
                position = columns[2].text.strip()
                table_data.append(f"{name}, {position}")

        # Kết hợp nội dung vào một chuỗi
        content = "\n".join(table_data)
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'hoi_dong_khoa_hoc_va_dao_tao.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content)
    else:
        print(f'Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}')

def crawl_hoi_dong_giao_su_co_so():
    # URL của trang cần crawl
    url = 'https://ptit.edu.vn/gioi-thieu/co-cau-to-chuc/hoi-dong-giao-su-co-so'

    # Gửi yêu cầu đến trang web
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tiêu đề của trang
        title = soup.title.string
        # truy cập vào phần body
        body = soup.find('div', class_="the_content_wrapper")

        # tìm bảng
        table_contents = []
        tables = body.find_all('table', class_="")
        for table in tables:
            table_data = []
            rows = table.find_all('tr')
            for row_id, row in enumerate(rows):
                columns = row.find_all('td')
                row_data = "";
                if columns:
                    for i in range(len(columns)):
                        row_data += columns[i].text.strip()
                        if i != len(columns) - 1:
                            row_data += ", "  
                table_data.append(row_data) 
            table_content = "\n".join(table_data)
            table_contents.append(table_content)

        # Kết hợp nội dung vào một chuỗi
        content = "\n\n".join(table_contents)
        # Lưu dữ liệu vào raw data folder
        output_file_path = os.path.join(DATA_FOLDER_PATH, 'hoi_dong_giao_su_co_so.txt')
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

def crawl_chtrinh_cntt_dinh_huong_ung_dung():
    url = 'https://daotao.ptit.edu.vn/chuong-trinh-dao-tao/chuong-trinh-cong-nghe-thong-tin-dinh-huong-ung-dung/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        
        body1 = soup.find('ul', class_='column_4 mtop')
        labels = body1.find_all('label')
        strongs = body1.find_all('strong')
        content_pairs = [f"{label.get_text()}: {strong.get_text()}" for label, strong in zip(labels, strongs)]
        content1 = "\n".join(content_pairs)

        body2 = soup.find('div', class_='ova_dir_content')
        content2 = body2.find_all(['section'])
        content1 += content2[0].get_text()
        content1 += content2[1].get_text()
        content1 += "\n"
        
        li_list = content2[2].find('ul', class_='nav-tab').find_all('li')
        content1 += li_list[0].get_text().strip()
        content1 += "\n"
        for  i in range(0, 8):
            hoc_ky = content2[2].find('div', id=f"tab-0-{i}")
            label = hoc_ky.find('label')
            content1 += label.get_text()
            content1 += "\n"
            so_tin = hoc_ky.find_all('div', class_='tag')
            mon_hoc = hoc_ky.find_all('div', class_='title')
            pairs = [f"{mon.get_text().strip()}: {tin.get_text().strip()}" for mon, tin in zip(mon_hoc, so_tin)]
            content_pair = "\n".join(pairs)
            content1 += content_pair
            content1 += "\n\n"
        content1 += li_list[1].get_text().strip()
        content1 += "\n"
        for  i in range(0, 8):
            hoc_ky = content2[2].find('div', id=f"tab-1-{i}")
            label = hoc_ky.find('label')
            content1 += label.get_text()
            content1 += "\n"
            so_tin = hoc_ky.find_all('div', class_='tag')
            mon_hoc = hoc_ky.find_all('div', class_='title')
            pairs = [f"{mon.get_text().strip()}: {tin.get_text().strip()}" for mon, tin in zip(mon_hoc, so_tin)]
            content_pair = "\n".join(pairs)
            content1 += content_pair
            content1 += "\n\n" 

        content1 += content2[3].get_text()
        content1 += content2[4].get_text()
        content1 += content2[5].get_text()
        
        this_labels = content2[6].find_all(['h3', 'label'])
        content1 += "\n"
        content1 += "\n".join(p.get_text() for p in this_labels)

        output_file_path = os.path.join(DATA_FOLDER_PATH, 'chtrinh_cntt_dinh_huong_ung_dung.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f'Tiêu đề: {title}\n\n')
            f.write(content1)
    else:
        print(f'Loi khong the truy cap trang. Ma trang thai: {response.status_code}')

if __name__ == '__main__':
    # crawl_lich_su_truyen_thong()
    # crawl_y_nghia_logo()
    # crawl_tam_nhin_su_mang()
    # crawl_triet_ly_giao_duc()
    # crawl_chien_luoc_phat_trien()
    # crawl_dang_uy_hoc_vien()
    # crawl_hoi_dong_hoc_vien()
    # crawl_ban_giam_doc_hoc_vien()
    # crawl_hoi_dong_khoa_hoc_va_dao_tao()
    # crawl_hoi_dong_giao_su_co_so()
    # crawl_nguon_nhan_luc()
    # crawl_co_so_vat_chat()
    crawl_chtrinh_cntt_dinh_huong_ung_dung()