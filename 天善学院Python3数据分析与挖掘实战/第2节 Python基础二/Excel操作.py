# xlrd,xlwt,xlsxwriter 不支持追加写入，openpyxl可以追加写入
import xlrd
from datetime import date,datetime
# 打开文件
workbook = xlrd.open_workbook(r'2003.xlsx')
# 获取所有sheet名
print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
# 获取所有sheet
for sheet in workbook.sheets():
    print(sheet.name,end=" ")

print()
# 根据sheet索引或者名称获取sheet内容
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
print(sheet1.name)
sheet2 = workbook.sheet_by_name('Sheet2')
print(sheet2.name)

# sheet的名称，行数，列数
print (sheet1.name, sheet1.nrows, sheet1.ncols)

# 获取整行和整列的值（数组）
rows = sheet1.row_values(3)  # 获取第四行内容
print(rows)
cols = sheet1.col_values(2)  # 获取第三列内容
print(cols)

# 获取单元格内容
print(sheet1.cell(1, 0).value)
print(sheet1.cell_value(1, 0))
print(sheet1.row(1)[0].value)

# 获取单元格内容的数据类型
# ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(sheet1.cell(1, 0).ctype)

#处理日期时，直接输出为浮点数
if (sheet1.cell(4,0).ctype == 3):
    # print(sheet1.cell(4,0).value)  43051.0
    # print(sheet1.cell_value(4,0))  43051.0
    date_value = xlrd.xldate_as_tuple(sheet1.cell_value(4,0),workbook.datemode)
    # print(date_value) (2017, 11, 12, 0, 0, 0)
    date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    #print(date_tmp)
#print('workbook.datemode'+str(workbook.datemode))

# 显示Excel合并单元格的部分，formatting_info=True 必须；merged_cells的四个参数row,row_range,col,col_range),
# 其中[row,row_range)包括row,不包括row_range,col也是一样，即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。
workbook11 = xlrd.open_workbook(r'2003.xlsx',formatting_info=True)
sheet2 = workbook11.sheet_by_index(0)
print(sheet2.merged_cells)
