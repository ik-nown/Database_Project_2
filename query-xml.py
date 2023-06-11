import xml.etree.ElementTree as ET

file_path=input("Đường dẫn đến file xml: ")
# đọc file từ path file
tree = ET.parse(file_path)
# lấy root ra
root = tree.getroot()

diem_thap = float(input("Nhập ngưỡng điễm thấp: "))
diem_cao = float(input("Nhập ngưỡng điểm cao: "))

xpath_expression = f".//Student[diem_tb]"

# Áp dụng XPath và lấy danh sách sinh viên
sinh_vien_list = root.findall(xpath_expression)

# In danh sách sinh viên
for sinh_vien in sinh_vien_list:
    ho_ten = sinh_vien.find("ho_ten").text
    # lấy điểm của sinh viên ra
    diem_tb = float(sinh_vien.find("diem_tb").text)
    #so sánh điều kiện vừa nhập với điểm của sinh viên.
    if diem_tb <= diem_cao and diem_tb >= diem_thap:
        print(f"Họ tên: {ho_ten}, Điểm TB: {diem_tb}")