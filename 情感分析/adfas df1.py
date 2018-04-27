from snownlp import SnowNLP
import pandas
import numpy
# header用来指定输出哪些列
data_txt=pandas.read_csv("test1.txt",sep="\t")
data_array=numpy.array(data_txt)
data_list=data_array.tolist()
sum=0
for chats_data in data_list:
    chats_data.append(0)
    for chat_data in chats_data[4].split('","'):
        chats_data[5] += 1
    sum+=chats_data[5]
print(sum)
140331

