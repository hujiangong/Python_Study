import xlrd
import os
import openpyxl

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        return files

foldername = str(r"新建文件夹")  # 被汇总的文件目录
resultname = str("汇总数据 20180212.xlsx")  # 汇总文件的文件名
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
    # for j in range(sheet_tmp.nrows):#这个用于通用型行数
    for j in range(row_num):  # 这个用于固定行数
        if j != 0 or i == 0:
            for k in range(len(sheet_tmp.row_values(j))):  # 这个用于通用型行数
                sheet_all.cell(row=all_row, column=k + 1, value=str(sheet_tmp.row_values(j)[k]))
            all_row = all_row + 1
    wb.save(resultname)
