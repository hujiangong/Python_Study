from snownlp import SnowNLP
#s=SnowNLP(u"这个东西，真心很赞") #u表示将后面跟的字符串以unicode格式存储。
# 分词
#print(s.words) #['这个', '东西', '真心', '很', '赞']
'''
# 标注词性
for tag in s.tags:
    print(tag)
('这个', 'r')
('东西', 'n')
('真心', 'd')
('很', 'd')
('赞', 'Vg')    

'''
# 输出正向概率
#print(s.sentiments) # positive的概率 0.9769551298267365

#输出汉子拼音
#print(s.pinyin) # ['zhe', 'ge', 'dong', 'xi', 'zhen', 'xin', 'hen', 'la', 'ji']

'''
# 繁体转简体
fanti=SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
print(fanti.han) # u'「繁体字」「繁体中文」的叫法
'''
'''
text = u"""
自然语言处理不是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
"""
text='足100也可以提现？;我点的是早点;是不是还要绑卡;谁知道你们系统怎么搞得 整出个石家庄外卖;天天用你们软件点外卖头一次碰到这种事;我是张家口市的;你们这个什么破系统;对;我也没吃上;我申请退款时随便填写的;转我微信吧;已经好了？;还有没有别的方式;我能吃的上吗;真麻烦;3876 7050 2773 0054 9;申请退款;不是;转我支付宝也行;我自己弄;不知道什么原因 你们系统却提示是给我石家庄的外卖信息;店家不给退款;我这申请退款也退不了;我在张家口;张家口点外卖怎么跑的石家庄了;你先充值了吧;可以吧;'
t = SnowNLP(text)
# 提取关键字
print(t.keywords(3)) # [u'语言', u'自然', u'计算机']
print(t.sentiments) # 竟然有1.0？
# 概要
print(t.summary(3)) # ['因而它是计算机科学的一部分', '自然语言处理不是计算机科学领域与人工智能领域中的一个重要方向', '自然语言处理是一门融语言学、计算机科学、数学于一体的科学']
# 句子
print(t.sentences)
'''
'''
t = SnowNLP([[u'这篇', u'文章'],
[u'那篇', u'论文'],
[u'这个',u'这个']])
# 词频，但不是总的，是每一个子list的词频
print(t.tf)
#逆向文件频率
print(t.idf)
print(t.sim([u'文章']))# [0.3756070762985226, 0, 0]
'''
# 当要分析的内容为空时，报ZeroDivisionError: division by zero错误
# print(SnowNLP("").sentiments)
data=";;;;;;;"
print(len(data.split(";")))

