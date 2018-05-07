from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
# 1、读取文档
txt1=open("绝世唐门2.txt","rb").read().decode("utf8")
txt2=open("绝世唐门3.txt","rb").read().decode("utf8")
# 2、对要计算的多篇文档进行分词
data1=jieba.cut(txt1,cut_all=False)
# data1,data2 为generator格式
data2=jieba.cut(txt2,cut_all=False)
data11=""
data21=""
# 3、将文档进行整理成指定格式，方便后续进行计算
for item in data1:
    data11+=item+" "
for item in data2:
    data21+=item+" "
# 4、计算出词语的频率
documents=[data11,data21] # 列表
# 这里将文本1中的词组成一个list，文本2中的组成一个list，然后两个list合并成二维list，即texts
texts=[[word for word in document.split()]
       for document in documents]
# 对词进行计数，即词频
# defaultdict(int) 创建一个默认的dict,其中value都是int型，默认值为0，key值自行确定
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
'''
# 5、【可选】对频率低的词语进行过滤
# 第一种结果：没有重复；只有词语重复三次以上的词；结果为字典格式
texts_over3={k:v for k,v in frequency.items() if v>3}
print(texts_over3)
'''
# 第二种结果：有重复；会对直接的分词结果进行循环；结果为list格式
texts_over3=[[word for word in text if frequency[word]>3]
 for text in texts]


# 6、通过语料库建立词典
# corpora.Dictionary(documents=None, prune_at=2000000)
# documents格式为list ？奇怪，明明是字典，为什么结果是list
# todo 往下开始的都看不懂
dictionary=corpora.Dictionary(texts_over3)
dictionary.save("dict.txt")

# 7、加载要对比的文档
txt3=open("绝世唐门5.txt","rb").read().decode("utf8")
data3=jieba.cut(txt3,cut_all=False)
data31=""
for item in data3:
    data31+=item+" "
# 8、将要对比的文档通过doc2bow转化为稀疏向量
new_vec=dictionary.doc2bow(data31.split())
# 9、对稀疏向量进行进一步处理，得到新的语料库
corpus=[dictionary.doc2bow(text) for text in texts_over3]
# 将corpora保存到本地
corpora.MmCorpus.serialize("corpus.mm",corpus)
# 10、将新语料库通过tf-idf算法进行处理，得到tf-idf
tfidf=models.TfidfModel(corpus)
# 11、通过token2id得到特征数
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vec]]
# 绝世唐门4 和2的相似性，绝世唐门4 和3的相似性，
print(sim) #[ 0.11869299  0.72905761]
'''
'''