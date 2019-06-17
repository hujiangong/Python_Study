# -*- coding: utf-8 -*-
# @Time : 2018/3/5 16:18
# @Author : HuJiangong
# @File : 不定量07版excel合并_bete2.py
# @Version : Python 3.6.4
# @Software: PyCharm
import xlrd
import os
import openpyxl
from tkinter import *
import tkinter.filedialog

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        return files

foldername = tkinter.filedialog.askdirectory() # 弹出式窗口选择文件夹
# foldername = str(r"新建文件夹")  # 被汇总的文件目录
resultname = str("20180314 解决能力定义校准表 汇总数据.xlsx")  # 汇总文件的文件名
titilename = str("Sheet1")  # 汇总文件的sheet页名字
row_num = 4

allfile = file_name(foldername)
wb = openpyxl.Workbook()
sheet_all = wb.active
sheet_all.title = titilename
all_row = 1
for i in range(len(allfile)):
    workbook_tmp = xlrd.open_workbook(foldername + "/" + allfile[i])
    sheet_tmp = workbook_tmp.sheet_by_index(0)
    print(allfile[i], ":", sheet_tmp.nrows)
    # if(sheet_tmp.nrows==4):
    #     row_num1=4
    # else:
    #     row_num1=5
    # for j in range(sheet_tmp.nrows):#这个用于通用型行数
    for j in range(row_num):  # 这个用于固定行数
        if j != 0 or i == 0:
            for k in range(len(sheet_tmp.row_values(j))):  # 这个用于通用型行数
                sheet_all.cell(row=all_row, column=k + 1, value=str(sheet_tmp.row_values(j)[k]))
            all_row = all_row + 1
    wb.save(resultname)
