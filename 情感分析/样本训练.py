# ！！！注意，训练完事以后需要将snownlp/sentiment/__init__.py里的data_path指向刚训练好的文件即可。别的训练相同
# 情感样本训练
from snownlp import sentiment
sentiment.train('neg1.txt','pos2.txt')
sentiment.save("D:\\Program Files (x86)\\Python\\Python36\\Lib\\site-packages\\snownlp\\sentiment\\sentiment_meituan.marshal")
## 分词训练
#from snownlp import seg
#seg.train("D:/Program Files (x86)/Python/Python36-32/Lib/site-packages/snownlp/seg/data.txt")
#seg.save("D:/Program Files (x86)/Python/Python36-32/Lib/site-packages/snownlp/seg/seg.marshal")
## 词性训练
#from snownlp import tag
#tag.train("D:/Program Files (x86)/Python/Python36-32/Lib/site-packages/snownlp/tag/199801.txt")
#tag.train("D:/Program Files (x86)/Python/Python36-32/Lib/site-packages/snownlp/tag/tag.marshal")