from aip import AipNlp
APP_ID = '10596297'
API_KEY = 'idHKvzjf8MWRc81DVeiq7cef'
SECRET_KEY = 'Pz9Wn6XKS7lwjFZZcyhG1ZwfiQDKvUsw'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

#建立连接的超时时间（单位：毫秒
#AipNlp.setConnectionTimeoutInMillis()
#通过打开的连接传输数据的超时时间（单位：毫秒）
#AipNlp.setSocketTimeoutInMillis()

#待分析文本（目前仅支持GBK编码），长度不超过65536字节
text="百度是一家高科技公司"
'''
词法分析：返回的格式为json字符串
参数名称	类型	必需	详细说明
text	string	是	原始单条请求文本
items	array(object)	是	词汇数组，每个元素对应结果中的一个词
+item	string	是	词汇的字符串
+ne	string	是	命名实体类型，命名实体识别算法使用。词性标注算法中，此项为空串
+pos	string	是	词性，词性标注算法使用。命名实体识别算法中，此项为空串
+byte_offset	int	是	在text中的字节级offset（使用GBK编码）
+byte_length	int	是	字节级length（使用GBK编码）
+uri	string	否	链指到知识库的URI，只对命名实体有效。对于非命名实体和链接不到知识库的命名实体，此项为空串
+formal	string	否	词汇的标准化表达，主要针对时间、数字单位，没有归一化表达的，此项为空串
+basic_words	array(string)	是	基本词成分
+loc_details	array(object)	否	地址成分，非必需，仅对地址型命名实体有效，没有地址成分的，此项为空数组。
++type	string	是	成分类型，如省、市、区、县
++byte_offset	int	是	在item中的字节级offset（使用GBK编码）
++byte_length	int	是	字节级length（使用GBK编码）
'''
#print(client.lexer(text))

""" 调用情感倾向分析 """
'''
参数	是否必须	类型	说明
text	是	string	输入的文本内容
items	是	array	输入的词列表
+sentiment	是	number	表示情感极性分类结果, 0:负向，1:中性，2:正向
+confidence	是	number	表示分类的置信度
+positive_prob	是	number	表示属于积极类别的概率
+negative_prob	是	number	表示属于消极类别的概率
'''
print(client.sentimentClassify(text))