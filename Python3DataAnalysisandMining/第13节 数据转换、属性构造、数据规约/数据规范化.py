import pymysql
import pandas as pa
import numpy as py
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="test")
sql="select price,comment from test"
data=pa.read_sql(sql,conn)
# 离差标准化
data2=(data-data.min())/(data.max()-data.min())
# 标准差标准化
data3=(data-data.mean())/data.std()
# 小数定标规范化
k=py.ceil(py.log10(data.abs().max()))
data4=data/10**(k)