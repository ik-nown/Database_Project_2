import random 
import mysql.connector
from collections import Counter
from random import randrange
from datetime import timedelta, datetime
import dataset as dataset
import math
import time

#hàm gen matr của từng học sinh
def generate_matr_of_hs(matr):
    matrhs = [] # list lưu matr từng học sinh, số lượng là 1tr
    for i in range(100):
        for x in range(10000):
            matrhs.append(matr[i])
    random.shuffle(matrhs) # làm xáo trộn các matr
#debugging: # print(len(matrhs))
            # print(matrhs[:10])
    return matrhs

# hàm nhận điểm trung bình và cho ra kết quả của năm học đó.
# dưới 5đ kết quả là chưa hoàn thành, ngược lại là hoàn thành
def xet_ket_qua(avg_score):
    ket_qua = " "
    if avg_score < 5.0: 
        ket_qua = "Chưa hoàn thành"
    else: 
        ket_qua = "Hoàn thành"
    return ket_qua

#hàm nhận điểm trung bình và cho ra xếp loại của năm học đó.
# với từng khoảng điểm đánh giá xếp loại khác nhau.
def xet_xep_loai(avg_score):
    xep_loai = ""
    if avg_score < 5.0:
        xep_loai = "Yếu"
    elif avg_score >= 5.0 and avg_score < 6.5:
        xep_loai="Trung bình"
    elif avg_score >= 6.5 and avg_score < 8.0:
        xep_loai="Khá"
    elif avg_score >= 8.0 and avg_score < 9.0:
        xep_loai ="Giỏi"
    elif avg_score >= 9.0 and avg_score <= 10.0:
        xep_loai ="Xuất Sắc"
    return xep_loai

