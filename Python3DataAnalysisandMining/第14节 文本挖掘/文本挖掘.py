import jieba
sentence="我喜欢上海的东方明珠"
'''
# cut_all=True 全模式；
print("--------------------全模式")
words=jieba.cut(sentence,cut_all=True)
for word in words:
    print(word)
# cut_all=False 精准模式；
print("--------------------精准模式")
words=jieba.cut(sentence,cut_all=False)
for word in words:
    print(word)

# 搜索引擎模式
print("---------------------搜索引擎模式")
words=jieba.cut_for_search(sentence)
for word in words:
    print(word)

# 词性标注 r：代词  v：动词  ns： a：形容词 c：连词  d：副词  e：叹词  f：方位词  i：成语  m：数词  n：名词  nr：人名  ns：地名 nt：机构团体
# nz：其它专有名词 p：介词 t：时间 u：助词 vn：动名词 w：标点符号 un：未知 s：处所词  b：区别词 
import jieba.posseg as psg
words=psg.cut(sentence)
for word in words:
    #也可以分开写word.word 是词，word.flag是词性
    print(word)

# 词典加载 txt文本必须为utf-8编码
jieba.load_userdict("")

# 更改词频
# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
jieba.add_word("更改词频") #增加词汇
'''
import jieba.analyse
# 提取文本中的关键词 ,第二个参数为提取几个关键词，默认20个
sentence="这个皮球弹性，这个皮鞋用料好，这个裤子弹好，这个房子特别"
print(jieba.analyse.extract_tags(sentence,3))
print(len("好".strip()) )
#
# #返回词语的位置
# word10=jieba.tokenize(sentence)
# for word in word10:
#     print(word)
# #以搜索引擎的方式返回位置
# word10=jieba.tokenize(sentence,mode="search")
# for word in word10:
#     print(word)