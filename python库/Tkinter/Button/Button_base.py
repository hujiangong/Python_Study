# Tkinter教程之Button篇(1)
# Button功能触发事件
'''''1.一个简单的Button应用'''
from tkinter import *

# 定义Button的回调函数
def helloButton():
    print('hello button')

root = Tk()
# 通过command属性来指定Button的回调函数
Button(root, text='Hello Button', command=helloButton).pack()
root.mainloop()

''''' 
执行的结果:每次点击一次，程序向标准输出打印'hello button',以上为Button使用方法，可以 
再做一下简化，如不设置Button的回调函数，这样也是允许的但这样的结果与Label没有什么太 
大的区别，只是外观看起来有所不同罢了，失去了Button的作用。 
from Tkinter import * 
root = Tk() 
#下面的relief = FLAT设置，就是一个Label了！！！ 
Button(root,text = 'hello button',relief=FLAT).pack() 
root.mainloop() 
'''
