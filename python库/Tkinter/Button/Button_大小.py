'''''5.指定Button的宽度与高度
width:    宽度
heigth:    高度
使用三种方式：
1.创建Button对象时，指定宽度与高度
2.使用属性width和height来指定宽度与高度
3.使用configure方法来指定宽度与高度
'''
from tkinter import *

root = Tk()
b1 = Button(root, text='30X1', width=30, height=2)
b1.pack()

b2 = Button(root, text='30X2')
b2['width'] = 30
b2['height'] = 3
b2.pack()

b3 = Button(root, text='30X3')
b3.configure(width=30, height=3)
b3.pack()

root.mainloop()
# 上述的三种方法同样也适合其他的控件
