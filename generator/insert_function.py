import mysql.connector
import time 
import random 
import generatehoc as hoc

# hàm connect với truonghoc1
def connect_to_db_truonghoc1():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", //nhập mật khẩu tại đây
        database="truonghoc1"
    )
    return connection

# hàm connect với truonghoc2
def connect_to_db_truonghoc2():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", //nhập mật khẩu tại đây
        database="truonghoc2"
    )   
    return connection


# hàm insert table truong của truonghoc1
# tham số: matr, tentr, dchitr
def insert_truong_to_truonghoc1(matr, tentr, dchitr):
    connection=connect_to_db_truonghoc1()
    cursor=connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement)
    start_time=time.time()
    values = [] # list lưu các statement
    print("Beginning insert data to table truonghoc1.`TRUONG`")
    for i in range(len(matr)):
        value = (matr[i], tentr[i], dchitr[i])
        values.append(value)
    sql= "INSERT INTO truong (matr, tentr, dchitr) VALUES (%s, %s, %s)"
    cursor.executemany(sql, values)
    connection.commit()
    connection.close()
    end_time=time.time()
    print("Thời gian insert vào bảng truonghoc1.`TRUONG`: \n" + str(end_time - start_time))
    print("Completed insert data to table truonghoc1.`TRUONG`")

#tương tự như hàm trên, nhưng đây là insert vào truonghoc2
def insert_truong_to_truonghoc2(matr,tentr,dchitr):
    connection= connect_to_db_truonghoc2()
    cursor=connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement) 
    values=[]
    start_time=time.time()
    print("Beginning insert data to table truonghoc2.`TRUONG`")
    for i in range(len(matr)):
        value = (matr[i], tentr[i], dchitr[i])
        values.append(value)
    sql= "INSERT INTO truong (matr, tentr, dchitr) VALUES (%s, %s, %s)"
    cursor.executemany(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    end_time=time.time()
    print("Thời gian insert vào bảng truonghoc2.`TRUONG`: \n" + str(end_time - start_time))
    print("Completed insert data to table truonghoc2.`TRUONG`")

# hàm insert vào table hs ở truonghoc1
# với 6 tham số: mahs, ho, ten, cccd, ntns, dchi_hs
def insert_hs_to_truonghoc1(mahs, ho, ten, cccd, ntns, dchi_hs):
    connection =connect_to_db_truonghoc1() # connect tới db
    cursor=connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement)
    start_time=time.time()
    values= []
    sql = "INSERT INTO hs (mahs, ho, ten, cccd, ntns, dchi_hs) VALUES (%s, %s, %s, %s, %s, %s)"
    print("Begining insert data to table truonghoc1.`HS`")

    for i in range(len(mahs)):
        val = (mahs[i], ho[i], ten[i], cccd[i], ntns[i], dchi_hs[i] )
        values.append(val)
        # cách execute 100000 một lần, rút ngắn thời gian insert
        if i % 100000 == 0:
            cursor.executemany(sql, values)
            values = []
    # trường hợp còn sót lại values.
    if len(values) !=0:
        cursor.executemany(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    end_time=time.time()
    print("Thời gian insert vào bảng truonghoc1.`HS`: \n" + str(end_time - start_time))
    print("Completed insert data to table truonghoc1.`HS`")

# hàm insert vào table hs truonghoc2.
# cách làm tương tự db truonghoc1.
def insert_hs_to_truonghoc2(mahs, ho, ten, cccd, ntns, dchi_hs):
    connection =connect_to_db_truonghoc2()
    cursor=connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement)
    start_time=time.time()
    values= []
    sql = "INSERT INTO hs (mahs, ho, ten, cccd, ntns, dchi_hs) VALUES (%s, %s, %s, %s, %s, %s)"
    print("Begining insert data to table truonghoc2.`HS`")
    for i in range(len(mahs)):
        val = (mahs[i], ho[i], ten[i], cccd[i], ntns[i], dchi_hs[i] )
        values.append(val)
        if i % 100000 == 0:
            cursor.executemany(sql, values)
            values = []
    if len(values) !=0:
        cursor.executemany(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    end_time=time.time()
    print("Thời gian insert vào bảng truonghoc2.`HS`: \n " + str(end_time - start_time))
    print("Completed insert data to table truonghoc2.`HS`")

#hàm insert vào table hoc của truonghoc1.
def insert_hoc_to_truonghoc1(matrhs, mahs, ntns):
    connection = connect_to_db_truonghoc1()
    cursor = connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement)
    start_time = time.time()
    print("Beginning insert data to truonghoc1.`HOC`: \n")
    sql = "INSERT INTO hoc (matr, mahs, namhoc, diemtb, xeploai, kqua) VALUES (%s, %s, %s, %s, %s, %s)"
    namhoc = ["2023", "2022", "2021"]
    values=[]
    # chia trường hợp dựa trên năm sinh.
    # sinh năm 2005 có 3 năm học, mỗi năm học có điểm tb, xeploai, kqua khác nhau

    for i in range(len(mahs)):
        if ntns[i][:4] == "2005":
            # loop random điểm tb cho 3 năm học
            for x in range(3):
                diemtb = round(random.uniform(3.5, 10),2) # random điểm tb
                if x >= 1:
                    #loop chặn việc các điểm tb quá chênh lệch nhau
                    while diemtb - list(values[i-1])[3] > 1.5:
                        diemtb = round(random.uniform(2, 10),2)
                xeploai = hoc.xet_xep_loai(diemtb)
                kqua = hoc.xet_ket_qua(diemtb)
                values.append((matrhs[i], mahs[i], namhoc[x], diemtb, xeploai, kqua))
        # học sinh sinh năm 2006 có 2 năm học
        elif ntns[i][:4] == "2006":
            for x in range(2):
                diemtb = round(random.uniform(3.5, 10),2)
                if x >= 1:
                    while diemtb - list(values[i-1])[3] > 1.5:
                        diemtb = round(random.uniform(2, 10),2)
                xeploai = hoc.xet_xep_loai(diemtb)
                kqua = hoc.xet_ket_qua(diemtb)
                values.append((matrhs[i], mahs[i], namhoc[x], diemtb, xeploai, kqua))
        # học sinh 2007 có 1 năm học.
        elif ntns[i][:4] == "2007":
            diemtb = round(random.uniform(2, 10),2)
            xeploai = hoc.xet_xep_loai(diemtb)
            kqua = hoc.xet_ket_qua(diemtb)
            values.append((matrhs[i], mahs[i], namhoc[0], diemtb, xeploai, kqua))
    # chia từng phần gồm 100000 dòng để execute
    val = []
    for v in values:
        val.append(v)
        
        if len(val) % 100000 == 0:
            cursor.executemany(sql, val)
            val = []
    if len(val)!= 0:
        cursor.executemany(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    end_time = time.time()
    print("Thời gian insert vào bảng truonghoc1.`HOC`: \n" + str(end_time - start_time))
    print("Completed insert data to table truonghoc1.`HOC`")
    return values # return để insert vào hoc ở truonghoc2

# tham số hàm insert này là tạo từ hàm insert_hoc_to_truonghoc1
# cách làm ở hàm này tương tự như hàm trên.
def insert_hoc_to_truonghoc2(values):
    connection = connect_to_db_truonghoc2()
    cursor = connection.cursor()
    sql_statement = "SET GLOBAL bulk_insert_buffer_size = 268435456;"
    cursor.execute(sql_statement)
    start_time = time.time()
    print("Beginning insert data to truonghoc2.`HOC`: \n")
    sql = "INSERT INTO hoc (matr, mahs, namhoc, diemtb, xeploai, kqua) VALUES (%s, %s, %s, %s, %s, %s)"
    val = []
    for v in values:
        val.append(v)
        #print(val)
        if len(val) % 100000== 0:
            cursor.executemany(sql, val)
            val = []
    if len(val)!= 0:
        cursor.executemany(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    end_time = time.time()
    print("Thời gian insert vào bảng truonghoc2.`HOC`: \n" + str(end_time - start_time))
    print("Completed insert data to table truonghoc2.`HOC`")

