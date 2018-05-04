import pandas
# TODO pandas.DataFrame()待学习
# pandas.DataFrame()
# Series：数据串
# x=pandas.Series([3,1,3,6])
# print(x)
# print(x.index)
# print(x.values)
# for inde in x.index:
    # print(str(inde)+':'+str(x[inde]))
    # print(inde)
    # print(x[inde])
# print(x[0])
'''
index data
0    3
1    1
2    3
3    6
dtype: int64
'''
# 指定索引
# x1=pandas.Series([3,1,3,6],index=["no1","no2","no3","no4"])
# x1.loc[1]['test']=9
# print(x1)

# DataFrame：数据框
y=pandas.DataFrame([[3,5,2,1],[2,6,8,11],[11,63,91]])
print(y)
list=[1,2,3,4,5,6,7,8,9]
x=pandas.DataFrame(list)
print(y)
#print(y)
'''
    0   1   2     3
0   3   5   2   1.0
1   2   6   8  11.0
2  11  63  91   NaN
'''
# 指定索引
y1=pandas.DataFrame([[3,5,2,1],[2,6,8,11],[11,63,91,23]],columns=["no1","no2","no3","no4"],index=["no11","no22","no33"])
#print(y1)
# 通过字典的方式创建DataFrame
#y2=pandas.DataFrame({
#    "one":2,
#    "two":[3,1,4],
#    "three":list(str(810))
#})
#print(y2)
'''
   one three  two
0    2     8    3
1    2     1    1
2    2     0    4
'''
# 头部数据，默认前五行
#y.head()
# y.head(2) #取前两行
# 尾部数据，默认后五行
#y.tail()
# y.tail(2) #取后两行
#print(y.describe())
'''
               0          1          2          3
count   3.000000   3.000000   3.000000   2.000000 #每列有多少个元素
mean    5.333333  24.666667  33.666667   6.000000 #平均数
std     4.932883  33.201406  49.742671   7.071068 #标准差
min     2.000000   5.000000   2.000000   1.000000 #最小值
25%     2.500000   5.500000   5.000000   3.500000 #前分位数
50%     3.000000   6.000000   8.000000   6.000000 #中分位数
75%     7.000000  34.500000  49.500000   8.500000 #后分位数
max    11.000000  63.000000  91.000000  11.000000 #最大值
'''
# 转置（行列转换）
#print(y.T)

'''
      no1  no2  no3  no4
no11    3    5    2    1
no22    2    6    8   11
no33   11   63   91   23
'''
# loc——通过行标签索引行数据
# 输出单行，第2行
#print(y.loc[1])
# 输出第2行及以后的
#print(y.loc[1:])
# 输出第2行到第3行
#print(y.loc[1:2])
# 通过行标签索引输出
#print(y1.loc["no11"])
#print(y1.loc["no22":])
# 某行某列(列使用数字报错)
#print(y1.loc["no22":,['no2']])
# 可以使用下面的方式取行列范围
#print(y1.loc["no22":,'no2':'no4'])
#print(y1.loc["no22":,[2]]) 不能这么写！
# 某列
#print(y1.loc[:,['no2','no4']])

'''
      no1  no2  no3  no4
no11    3    5    2    1
no22    2    6    8   11
no33   11   63   91   23
'''
# iloc——通过行号获取行数据
# 1、普通行号
#print(y1.iloc[1])
# 通过标签索引会报错
# print(y1.iloc["no11"])
# 其余用法和loc一样。只不过只能用普通索引，超出范围并不会报错。
#print(y1.iloc[1:10])
#print(y1.iloc[:,[0,2]]) # 列只能用逗号，不能用冒号取范围的

#ix——结合前两种的混合索引
#print(y1.ix[1:10])
#print(y1.ix["no22":"no33"])
#print(y1.ix["no22":"no33",[0,2]]) # 取特定的列
# 当使用标签索引时，范围为[]，当使用数字索引时，范围为[)，好奇怪！
# print(y1.ix["no22":"no33",0:1])
# print(y1.ix[0:0,0:1])