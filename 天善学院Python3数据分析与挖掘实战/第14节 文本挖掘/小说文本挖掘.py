import jieba.analyse
data=open("test.txt","rb")
# data=open("teset1.txt")
data2=data.read().decode("utf8")
print(data.readlines())
# 提取20个关键字
# for datae in data2:
#     print(datae)
# guanjianzi=jieba.analysese.extract_tags(data2,20)
# for gjz in guanjianzi:
#     print(gjz)