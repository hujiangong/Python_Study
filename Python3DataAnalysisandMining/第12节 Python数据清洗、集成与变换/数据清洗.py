import pymysql
import numpy
import pandas as pad
import matplotlib.pylab as pyl
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="test")
sql="select * from test"
data=pad.read_sql(sql,conn)
# 展现数据的基础信息
print(data.describe())
# 展现数据的行数，有可能和describe中的count不同，即可得到缺失值
len(data)

x=0
# 当data的列名2为0的时候将列名1的数据赋为None
data["列名1"][(data["列名2"]==0)]=None
for i in data.columns:#列数
    for j in range(len(data)):# 行数
        # TODO 未懂
        if (data[i].isnull())[j]:
            data[i][j]="36"
            x+=1

# 异常值处理
# 画散点图（横轴为价格，纵轴为评论数）
# 得到价格
data2=data.T
price=data2.values[2]
# 得到评论数
comt=data2.values[3]
pyl.plot(price,comt,"o")
pyl.show()
# 根据图形观察以后，觉得评论数>200000，价格>2300为异常数据，可以进行清理
line=len(data.values) # 行
col=len(data.values[0]) # 列
data3=data.values
# 循环清理异常数
for i in range(0,line):
    for j in range(0,col):
        if(data3[i][2]>=2300):
            data3[i][j]=36 # 中位数 ??这里为什么都设置为一个中位数
            # data3[i][2]=36
        if(data3[i][3]>200000):
            data3[i][j]=58
#重新绘制
data4=data3.T
price2=data2.values[2]
comt2=data2.values[3]
pyl.plot(price2,comt2,"o")
pyl.show()

# 分布分析
pricemax=data4[2].max()
pricemin=data4[2].min()
commentmax=data4[3].max()
commentmin=data4[3].min()
# 极差：最大值-最小值
pricerg=pricemax-pricemin
commentrg=commentmax-commentmin
# 组距: 极差/组数
pricedst=pricerg/12
commendst=commentrg/12
#画价格的直方图
pricesty=numpy.arange(pricemin,pricemax,pricedst)
pyl.hist(data4[2],pricesty)
pyl.show()
#画评论的直方图
commentsty=numpy.arange(commentmin,commentmax,commendst)
pyl.hist(data4[3],commentsty)
pyl.show()
