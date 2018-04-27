'''6.设置Button文本在控件上的显示位置
anchor：
使用的值为:n(north),s(south),w(west),e(east)和ne,nw,se,sw，就是地图上的标识位置了，使用
width和height属性是为了显示各个属性的不同。
'''
from tkinter import *

root = Tk()

# 简单就是美！
for a in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
    Button(root,
           text='anchor',
           anchor=a,
           width=30,
           height=4).pack()
# 如果看的不习惯，就使用下面的代码。
# Button(root,text = 'anchor',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'center',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'n',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 's',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'e',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'w',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'ne',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'nw',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'se',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'sw',width = 30,height = 4).pack()

root.mainloop()
