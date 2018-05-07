import pymysql
import pandas as pa
import numpy as py
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="test")
sql="select price from test"
data=pa.read_sql(sql,conn)
data2=data.T
data3=data2.values
# 划分的份数；5即等宽划分为5份
num=5
# labers 每份的标签名
pa.cut(data3,num,labels=["第一标签","第二标签","第三标签","第四标签","第五标签"])
# 手动指定范围划分；(3,6],(6,9],(9,13] 范围外的不算
pa.cut(data3,[3,6,9,13])