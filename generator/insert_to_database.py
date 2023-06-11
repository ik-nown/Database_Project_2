import generate_db as db
import insert_function as insert
# CHỈ CẦN CHẠY FILE NÀY THÌ TẤT CẢ DỮ LIỆU SẼ ĐƯỢC GENERATE VÀ INSERT TRỰC TIẾP VÀO DATABASE.

# tạo các dữ liệu cần thiết 
matr=db.matr
tentr=db.tentr
dchitr=db.dchitr
#insert vào trường ở cả 2 databases.
insert.insert_truong_to_truonghoc1(matr, tentr, dchitr)
insert.insert_truong_to_truonghoc2(matr, tentr, dchitr)

mahs = db.mahs
ho= db.ho
ten= db.ten
cccd = db.cccd
ntns = db.ntns
dchi_hs = db.dchi_hs

# insert vào hs ở cả 2 databases
insert.insert_hs_to_truonghoc1(mahs, ho, ten, cccd, ntns, dchi_hs)
insert.insert_hs_to_truonghoc2(mahs, ho, ten, cccd, ntns, dchi_hs)

#gen ngẫu nhiên mã trường cho 1tr học sinh.
matrhs = db.matrhs
#insert vào hoc ở cả hai database.
#do 2 data ở 2 db là giống nhau nên trả về values để tiếp tục insert vào truonghoc2.
values = insert.insert_hoc_to_truonghoc1(matrhs, mahs, ntns)
insert.insert_hoc_to_truonghoc2(values)

