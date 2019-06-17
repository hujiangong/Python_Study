# -*- coding: utf-8 -*-
# @Time : 2018/3/20 17:11
# @Author : HuJiangong
# @File : 替换Unicode中的emoji.py
# @Version : Python 3.6.4
# @Software: PyCharm

import re

try:
    # Wide UCS-4 build
    myre = re.compile(u'['
                      u'\U0001F300-\U0001F64F'
                      u'\U0001F680-\U0001F6FF'
                      u'\u2600-\u2B55]+',
                      re.UNICODE)
except re.error:
    # Narrow UCS-2 build
    myre = re.compile(u'('
                      u'\ud83c[\udf00-\udfff]|'
                      u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                      u'[\u2600-\u2B55])+',
                      re.UNICODE)

# 腾讯视频用的一般是UCS-2 的，所有可以直接用except中的
myre = re.compile(u'('
                  u'\ud83c[\udf00-\udfff]|'
                  u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                  u'[\u2600-\u2B55])+',
                  re.UNICODE)

sss = u'I have a dog \U0001f436 . You have a cat \U0001f431 ! I smile \U0001f601 to you!'
sss = u'\u6f14\u674e\u5c0f\u5189\u7236\u4eb2\u7684\u771f\u662f\u8001\u620f\u9aa8\u62b1\u6b49\u90fd\u4e0d\u77e5\u9053\u540d\u5b57\u3002\u6f14\u5f97\u771f\u6b22\u4e50\u554a~ \u674e\u4e43\u6587\u4e5f\u662f\u6760\u6760\u7684\ud83d\udc4d'
print(myre.sub('[Emoji]', sss))  # 替换字符串中的Emoji
print(myre.findall(sss))  # 找出字符串中的Emoji
