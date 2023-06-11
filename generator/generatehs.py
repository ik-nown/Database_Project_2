import random 
import mysql.connector
from collections import Counter
from random import randrange
from datetime import timedelta, datetime
import dataset as dataset
import math
import time

#gen mã học sinh, số lượng là 1tr
def generate_mahs():
    #dùng set để ngăn chặn việc trùng mã học sinh
    numbers = set()
    while len(numbers) < 1000000:
        number = random.randint(100000000, 999999999)
        numbers.add('0' + str(number))
    return numbers
#hàm gen cùng lúc họ và tên cho học sinh
def generate_ho_ten_hs():
    ho=[]
    ten=[]
    for i in range(1000000):
        hohs=random.sample(dataset.ho, 1)
        hohs0=hohs[0]
        # giới hạn để sinh học kép.
        if (i > 600000):
            hohs1=random.sample(dataset.ho,1)
            # vòng lặp tránh họ kép gồm 2 họ giống nhau
            while hohs1[0] == hohs0:
                hohs1=random.sample(dataset.ho,1)
            ho_kep = hohs0 + " " + hohs1[0]
            ho.append(ho_kep)
        else:
            ho.append(hohs0)
        tenhs=random.sample(dataset.name, 1)
        ten.append(tenhs[0])
    return ho, ten

# gen cccd cho các học sinh
# đầu cccd là 087
def generate_cccd():
    cccds = set() # dùng set để tránh trùng cccd
    while len(cccds) < 1000000:
        number=random.randint(87000000001,88000000000)
        cccds.add('0' + str(number))
    return cccds

# gen date, độ tuổi là 2005 - 2007, là lớp 10 đến lớp 12
def generate_date():
    year_start = datetime(2005, 1, 1) 
    year_end = datetime(2007, 12, 31)
    delta = year_end - year_start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return year_start + timedelta(seconds=random_second)

# hàm gen 1tr ngày sinh cho 1tr học sinh
def generate_ntns():
    ntns=[]
    for i in range(1000000):
        ngaysinh=generate_date().strftime('%Y-%m-%d')
        ntns.append(ngaysinh)
    return ntns

# hàm gen địa chỉ cho 1tr hs, gồm phường, quận, thành phố
def generate_diachi_hs():
    dchihs = []
    tinh="Hồ Chí Minh"
    for i in range(1000000):
        quan = random.choice(dataset.quan)
    # Kiểm tra quận để lấy tên phường/phường tương ứng
        if quan == "Thủ Đức":
            phuong = random.choice(dataset.phuong_thuduc)
        elif quan == "Quận 1":
            phuong = random.choice(dataset.phuong_quan1)
        elif quan == "Quận 4":
            phuong = random.choice(dataset.phuong_quan4)
        elif quan == "Quận 7":
            phuong = random.choice(dataset.phuong_quan7)
        elif quan == "Quận 5":
            phuong = random.choice(dataset.phuong_quan5)
        diachi_hs = phuong + " , " + quan + " , " + tinh + "."
        dchihs.append(diachi_hs)
    return dchihs