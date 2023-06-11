import random 
import mysql.connector
from collections import Counter
from random import randrange
from datetime import timedelta, datetime
import dataset as dataset
import math
import time
#gen 100 mã trường, với đầu 28 do trường nằm trong địa bàn TP HCM
def generate_ma_truong():
    matr = []
    for index in range(28000, 28100):
        matr.append(index)
    return matr
# gen 100 tên trường, chọn ngẫu nhiên từ bộ dữ liệu truong trong file dataset
def generate_ten_truong():
    unique_dataset_truong=list(set(dataset.truong))
    tentr=random.sample(unique_dataset_truong, 100)
    return tentr

#Gen 100 địa chỉ trường tương ứng với 100 trường và lưu vào list dchitr
def generate_diachi_truong():
    dchitr = []
    # nằm trong duy nhất tp hcm
    tinh="Hồ Chí Minh"
    #gen ngẫu nhiên 120 địa chỉ(đang tạo dataset địa chỉ)
    for i in range(120):
    # chọn 1 trong 5 quận trong dataset.quan
        quan = random.choice(dataset.quan)
    # Kiểm tra quận để lấy tên phường/phường tương ứng
        if quan == "Thủ Đức":
            # chọn 1 phường trong dataset phường của quận thủ đức
            phuong = random.choice(dataset.phuong_thuduc)
        elif quan == "Quận 1":
            # chọn 1 phường trong dataset phường của quận 1
            phuong = random.choice(dataset.phuong_quan1)
        elif quan == "Quận 4":
            # chọn 1 phường trong dataset phường của quận 4
            phuong = random.choice(dataset.phuong_quan4)
        elif quan == "Quận 7":
            # chọn 1 phường trong dataset phường của quận 7
            phuong = random.choice(dataset.phuong_quan7)
        elif quan == "Quận 5":
            # chọn 1 phường trong dataset phường của quận 5
            phuong = random.choice(dataset.phuong_quan5)
        #chọn ngẫu nhiên 1 tên đường trong dataset.duong
        duong= random.choice(dataset.duong)
        #ghép các tên đã chọn được
        diachi_truong = duong + " , " + phuong + " , " + quan + " , " + tinh + "."
        dchitr.append(diachi_truong)
    #set() để loại bỏ các địa chỉ trùng, sau đó chọn 100 địa chỉ từ set và đổi thành type list
    dchitr=list(set(dchitr))[:100]
    return dchitr