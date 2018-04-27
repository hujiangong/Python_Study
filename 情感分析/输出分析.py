from snownlp import SnowNLP
import pandas
import numpy
# header用来指定输出哪些列
#data_pandas=pandas.read_excel("12-19只用户聊天记录1.xlsx",sheet_name="Sheet1")
data_txt=pandas.read_csv("12-19chat_collect_list.txt",sep="\t")
data_array=numpy.array(data_txt)
data_list=data_array.tolist()
#for chats_data in data_list:
#    chats_data.append(0)
#    for chat_data in chats_data:
#        print(chat_data)#
#    break
def cou(data_list):
    for chats_data in data_list:
        chats_data.append(0)
        for chat_data in chats_data[4].split('","'):
            try:
                chats_data[5]+=SnowNLP(chat_data).sentiments
                #SnowNLP(chat_data).sentiments
                #print(chat_data)
            except Exception as err:
                print(err)
                print(chats_data[0:4])
                #return
        chats_data.append(chats_data[5]/len(chats_data[4].split('","')))
cou(data_list)
#result_list=numpy.delete(numpy.array(data_list),4,axis=1).tolist()
result_array=numpy.delete(numpy.array(data_list),4,axis=1)
df=pandas.DataFrame(result_array)
df.to_excel("情感结果.xlsx",sheet_name='Resutl Data')

