# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import pandas
import numpy
import re
str=u'''  '''
'''
for chat_data in str.split(";"):
    try:
        SnowNLP(chat_data).sentiments
        print(chat_data)
    except Exception as err:
        print(err)
        break
        '''
# df=pandas.DataFrame([[1,2],[2,3],[3,4]])
# df.to_excel("结果.xlsx",sheet_name='Random Data')
#list3=[0,2]
#list=[[1,2],[2,3],[3,4]]
#np=numpy.array(list)
#np2=numpy.delete(np,1,axis=0)
#print(np2)

#SnowNLP.sentiments()
# re_zh = re.compile('([\u4E00-\u9FA5]+)')
# words=[]
# sent=u"更别说评论，而且4星还是非常满意，还是要降！"
# s="4"
# if not s:
#     print("True")
# else:
#     print("False")

# for s in re_zh.split(sent):
#     print("分词结果:",s)
#     if not s:
#         print("True")
#         continue
#     if re_zh.match(s):
#         print("ad")
        #words += single_seg(s)
    #print(s.strip())
#def seg(sent):
#    words = []
#    for s in re_zh.split(sent):
#        s = s.strip()
#        if not s:
#            continue
#        if re_zh.match(s):
#            words += single_seg(s)
#        else:
#            for word in s.split():
#                word = word.strip()
#                if word:
#                    words.append(word)
#    return words


#data_txt=pandas.read_csv("12-19chat_collect_list.txt",sep="\t")
#print(data_txt)

# s = pandas.Series(numpy.random.randn(5), index = list('ABCDE'))
# print(s)
#print(s[s > s.median()])
#print(s[[4, 2, 1]])
# print(numpy.exp(s))
import math
# print(math.exp(2))
# print(math.e*math.e)
# print(math.exp(-2))
print(math.log(math.e))