import pandas as pd
import numpy
from snownlp import SnowNLP
data_pandas=pd.read_excel("12-11聊天记录1.xlsx",sheet_name="测试样本",header=0)
# pandas 转NumPy的ndarray数组对象,有下面两种方法
data_array = numpy.array(data_pandas)#np.ndarray()
#data_array=data_pandas.iloc[:,:].values
# NumPy的ndarray数组对象转list(因为数组不可调整)
data_list=data_array.tolist()
for data in data_list:
    s=SnowNLP(data[0])
    data.append(1 if s.sentiments>0.5 else 0)
    #print(data)

error=0
true=0
for data in data_list:
    if data[1]==data[2]:
        true += 1
    else:
        print(data)
        error += 1
print(true)
print (str(true/(true+error)))

