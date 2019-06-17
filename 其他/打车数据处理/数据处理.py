# -*- coding: utf-8 -*-
# @Time : 2018/5/2 19:06
# @Author : HuJiangong
# @File : 数据处理.py
# @Version : Python 3.6.4
# @Software: PyCharm

import pandas
def allorder():
    pd=pandas.read_table("file1.txt")
    lng_lat=pd['lng+lat'].value_counts()
    file_tmp=open("d:/file1.txt","w")
    for index in lng_lat.index:
        str_temp=str(index)+ ',"count":' + str(lng_lat[index]) + '},'
        file_tmp.write(str_temp + '\n')
    file_tmp.close()


def cancel():
    new_list=list()
    pd = pandas.read_table("cancel.txt")
    file_tmp = open("d:/file2.txt", "w")
    for i in range(0,len(pd['用户定位开始位置经度'])):
        str_temp = '{"lng":' + str(pd['用户定位开始位置经度'].loc[i])[0:3] +'.'+ str(pd['用户定位开始位置经度'].loc[i])[3:] + ',"lat":' + str(pd['用户定位开始位置纬度'].loc[i])[0:2] +'.'+str(pd['用户定位开始位置纬度'].loc[i])[2:]
        file_tmp.write(str_temp + '\n')
        # new_list.append(str_temp)
        # print(new_list)
    # list_pd=pandas.DataFrame(new_list)
    # print(list_pd)
    # new_pd=pandas.concat([pd,list_pd],axis=1)
    # for i in (0,len(new_pd)):
    #     file_tmp.write(str(new_pd['0'].loc[i])+'\n')
        # file_tmp.write(str(new_pd.loc[i]) + '\n')
    file_tmp.close()
# cancel()

def allorder1():
    pd=pandas.read_table("cancel_tmp")
    lng_lat=pd['lng+lat'].value_counts()
    file_tmp=open("d:/file3.txt","w")
    for index in lng_lat.index:
        str_temp=str(index)+ ',"count":' + str(lng_lat[index]) + '},'
        file_tmp.write(str_temp + '\n')
    file_tmp.close()
allorder1()
#
# file_tmp.close()
# print(type(pd['用户定位开始位置经度'].value_counts())) # <class 'pandas.core.series.Series'>
# for value in pd['用户定位开始位置经度'].value_counts().index:
    # pd['用户定位开始位置经度'].value_counts()[value]
    # print(str(value)+':'+pd['用户定位开始位置经度'].value_counts()[value])
    # print(value)

    # def _map(data, exp):
    #     for index, row in data.iterrows():  # 获取每行的index、row
    #         for col_name in data.columns:
    #             row[col_name] = exp(row[col_name])  # 把结果返回给data
    #     return data
    # print(index)
# string1='118869588'
# new=string1[0:3]+'.'+string1[3:]
# print(new)
# file=open("d:/file1.txt","w")
# file.write('123'+'\n')
# file.write('234')
# file.close()
# 维度查看
# print(pd.shape)
# # 基本信息
# print(pd.info())
# # 每一列数据的格式
# print(pd.dtypes)
# # 某一列的格式
# print(pd['用户定位开始位置经度'].dtype)
# # 空值
# print(pd.isnull())
# # 查看某一列的空值
# print(pd['用户定位开始位置经度'].isnull())
# # 查看某一列的唯一值
# print(pd['用户定位开始位置经度'].unique())
# # 查看数据表的值
# print(pd.values)
# # 查看列名称
# print(pd.columns)
# # 前后头、尾数据，默认10行
# print(pd.head(10))
# print(pd.tail(10))

# print(pd.head(5))