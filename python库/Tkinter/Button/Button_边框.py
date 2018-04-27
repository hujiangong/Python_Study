'''8.设置Button的边框
bd(bordwidth):缺省为1或2个像素
'''
from tkinter import *

root = Tk()
# 创建5个Button边框宽度依次为：0，2，4，6，8
for b in [0, 1, 2, 3, 4]:
    Button(root,
           text=str(b),
           bd=b).pack()

root.mainloop()
