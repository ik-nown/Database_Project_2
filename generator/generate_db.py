import random 
from random import randrange
from datetime import timedelta, datetime
import dataset as dataset
import time
import generatetruong as truong
import generatehs as hs
import generatehoc as hoc

# các hàm generate được đóng gói trong các file python cùng thư mục này.
# trong đó generatetruong chứa các hàm gen dữ liệu cho bảng truong
# generatehs chứa các hàm gen dữ liệu cho bảng hs
# và generatehoc chứa các hàm gen dữ liệu cho bảng hoc
#
# 
#generate các dữ liệu cho các bảng
start= time.time() # đo thời gian gen.

print("Bắt đầu gen dữ liệu: ")
# lưu vào các list để còn sử dụng lại.
matr = truong.generate_ma_truong()
tentr = truong.generate_ten_truong()
dchitr = truong.generate_diachi_truong()

end_truong=time.time()
print("Thời gian gen dữ liệu cho bảng trường: \n" + str(end_truong - start))
# gen dữ liệu cho bảng truong
start= time.time()

mahs=list(hs.generate_mahs())
ho, ten = hs.generate_ho_ten_hs()
cccd = list(hs.generate_cccd())
ntns = hs.generate_ntns()
dchi_hs = hs.generate_diachi_hs()

end_hs=time.time()
print("Thời gian gen dữ liệu cho bảng hs: \n" + str(end_hs- start))

# Ở bảng HOC chỉ cần gen thêm mã trường cho các học sinh
# do sử dụng lại mahs và dchihs đã gen trước đó.

start=time.time()

matrhs=hoc.generate_matr_of_hs(matr)

end_hoc=time.time()
print("Thời gian gen dữ liệu cho bảng học: \n" + str(end_hoc- start)
      + "\n Kết thúc quá trình gen dữ liệu")

# tất cả dữ liệu được gen ở file này được insert vào cả 2 database.


