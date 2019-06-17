# -*- coding: utf-8 -*-
# @Time : 2018/4/30 19:31
# @Author : HuJiangong
# @File : 多线程.py
# @Version : Python 3.6.5
# @Software: PyCharm
import time
import threading

#可能是因为电脑运行速度过快，不使用休眠1秒看不出来多线程效果

class A(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        for i in range(0,10):
            print(self.name)
            time.sleep(1)
class B(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        for i in range(0,10):
            print(self.name)
            time.sleep(1)
threadA=A("threadA")
threadA.start()
threadB=B("threadB")
threadB.start()
