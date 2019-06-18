# -*- coding: utf-8 -*-
# @Time : 2018/7/20 9:48
# @Author : HuJiangong
# @File : 闭包.py
# @Version : Python 3.6.4
# @Software: PyCharm


def outer():
    test = 'hello'

    def inner():
        print (test)
    #     test = 'hello'
        print(eval("test == 'hello'"))

    inner()

if __name__ == '__main__':
    outer()
