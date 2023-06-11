import mysql.connector
import time
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
def query_students(database_name, tentr, namhoc, xeploai):
    # Tạo tên tệp XML theo quy ước
    xml_filename = "XML/" + f"{database_name}-{tentr}-{namhoc}-{xeploai}.xml"

    # Thiết lập kết nối tới cơ sở dữ liệu MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12012004vert',
        database = database_name
    )
    cursor = conn.cursor()

    # Đo thời gian truy vấn dữ liệu
    start_time = time.time()

    # Truy vấn dữ liệu từ cơ sở dữ liệu
    query = f"SELECT CONCAT_WS(' ', ho, ten) as hoten, ntns, diemtb, xeploai, kqua FROM truong, hs, hoc WHERE hs.mahs=hoc.mahs and truong.matr=hoc.matr and truong.tentr = %s AND namhoc = %s AND xeploai = %s;"
    params = (tentr, namhoc, xeploai)

    cursor.execute(query, params)
    results = cursor.fetchall()

    end_time = time.time()
    query_time = end_time - start_time

    # # In danh sách học sinh
    for result in results:
        ho_ten, ntns, diem_tb, xep_loai, ket_qua = result
        print(f"Họ tên: {ho_ten}, NTNS: {ntns}, Điểm TB: {diem_tb}, Xếp loại: {xep_loai}, Kết quả: {ket_qua}")
    
    # in số luợng query được
    print(len(results))

    # Tạo cấu trúc XML và ghi dữ liệu vào tệp XML
    root = ET.Element("Students") # root element
    # duyệt qua từng thành phần được query được từ database
    for result in results:
        # mỗi student là con của root Students
        student = ET.SubElement(root, "Student")
        # các element của nhánh student
        ho_ten, ntns, diem_tb, xep_loai, ket_qua = result
        ET.SubElement(student, "ho_ten").text = ho_ten
        ET.SubElement(student, "ntns").text = str(ntns)
        ET.SubElement(student, "diem_tb").text = str(diem_tb)
        ET.SubElement(student, "xep_loai").text = xep_loai
        ET.SubElement(student, "ket_qua").text = ket_qua

    tree = ET.ElementTree(root)
    # lưu xml thành string
    xml_str = ET.tostring(root, encoding="utf-8")

    parsed_xml = minidom.parseString(xml_str)

    # Format xml đẹp hơn
    pretty_xml_str = parsed_xml.toprettyxml(indent="    ")

    # ghi vào file xml
    with open(xml_filename, "w", encoding="utf-8") as xml_file:
        xml_file.write(pretty_xml_str)

    # Đóng kết nối cơ sở dữ liệu
    cursor.close()
    conn.close()
    return query_time

# nhập các tham số
n = input("Nhập số lần query: ")

# duyệt qua số lần query
for i in range(int(n)):
    database_name = input("Tên database lần " + str(i) + " : ")
    field_name = input("Tên trường lần " + str(i) + " : ")
    academic_year = input("Năm học lần " + str(i) + " : ")
    academic_rank = input("Xếp loại lần " + str(i) + " : ")
    query_time = query_students(database_name, field_name, academic_year, academic_rank)
    print(f"Thời gian truy vấn lần " + str(i) +" : "+ f"{query_time} giây")
