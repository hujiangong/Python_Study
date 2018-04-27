'''10.设置Button状态
normal/active/disabled
'''
from tkinter import *

root = Tk()

def statePrint():
    print('state')

for r in ['normal', 'active', 'disabled']:
    Button(root,
           text=r,
           state=r,
           width=30,
           command=statePrint).pack()

# 例子中将三个Button在回调函数都设置为statePrint,运行程序只有normal和active激活了回调函数，而disable按钮则没有，对于暂时不
# 需要按钮起作用时，可以将它的state设置为disabled属性
root.mainloop()
