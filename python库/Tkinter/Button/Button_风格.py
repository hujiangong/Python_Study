'''''2.测试Button的relief属性'''
# 运行下面的代码可以看到Button的各个不同效果，均没有回调函数。
from tkinter import *

root = Tk()
# flat, groove, raised, ridge, solid, or sunken
Button(root, text='hello button', relief=FLAT).pack()
Button(root, text='hello button', relief=GROOVE).pack()
Button(root, text='hello button', relief=RAISED).pack()
Button(root, text='hello button', relief=RIDGE).pack()
Button(root, text='hello button', relief=SOLID).pack()
Button(root, text='hello button', relief=SUNKEN).pack()

root.mainloop()
