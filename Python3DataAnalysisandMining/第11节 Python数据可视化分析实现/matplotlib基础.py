import matplotlib.pylab as pyl
import numpy as npy
# x=[1,2,3,4,5]
# y=[3,5,2,1,5]
# 折线图 plot(x轴,y轴,展现形式(颜色等),)
# 线条样式
# - 直线
# --虚线
# -. -.形式
# ： 细小虚线
#pyl.plot(x,y)
#pyl.show()
# 散点图 参数o为散点图
'''
点的形式
s 方形
h 六角形
H 六角形
* 星号
+ 加号
d 菱形
D 菱形
p 五角形
'''
#pyl.plot(x,y,"o")
#pyl.show()
'''
pyl.plot(x,y,":o")
# 标题
pyl.title("title")
# x 标签
pyl.xlabel("x轴")
# x轴范围
pyl.xlim(0,10)
# y 标签
pyl.ylabel("y轴")
# y轴范围
pyl.ylim(0,13)
# 第二条线段
x=[3,5,2,6,1]
y=[6,4,8,5,10]
pyl.plot(x,y,":o")
'''
# 随机数的生成
# x2=npy.random.randint(1,10,7) # 最大值，最小值，个数
# y2=npy.random.randint(1,10,7)
# pyl.plot(x2,y2,":o")
# pyl.show()
# normal()输出正态分布的数据
# data=npy.random.normal(4.2,2.0,10) # 均数，西格玛，个数
# print(data)

# 直方图
data3=npy.random.normal(10.0,2.0,1000)
# 最小值，最大值，步长(直方图中的列宽)
sty=npy.arange(2,10,1)
# histtype用来设置列之间的界限线，默认为bar，设置为stepfilled则去掉分界线(现在设置为啥都没有分界线)
pyl.hist(data3,histtype="stepfilled")
# 将整个区域拆分为多少行，多少列，图形绘制在第几个区域
pyl.subplot(2,2,1) # 四象限中的第一象限
# 在这里绘制第一象限的图形
pyl.subplot(2,2,2) # 四象限中的第二象限
pyl.subplot(2,1,2) # 四象限中的第三四合并象限
pyl.show()