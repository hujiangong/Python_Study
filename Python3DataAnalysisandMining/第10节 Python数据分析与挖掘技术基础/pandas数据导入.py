import pandas
# csv导入
#csv_file=pandas.read_csv("")
#csv_file.describe() #数据详情
#csv_file.sort_values(by="列名") # 按列名排序
#csv_file.sort_index(by=1) # 按列数排序
#
## Excel导入
#excel_file=pandas.read_excel()

# mysql导入
import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="test")
sql="select * from test"
rs=pandas.read_sql(sql,conn)
print(rs)

# 网页数据导入
# 需要html5lib、beautifulsoup4 包
m=pandas.read_html("https://book.douban.com") # 只有表格标签<table>
print(m)

# 文本导入
pandas.read_table("***.csv")

# 读取Excel
testdata=pandas.read_excel("12-11聊天记录1.xlsx",sheet_name="测试样本",header=0)