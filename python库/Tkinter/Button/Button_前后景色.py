'''7.改变Button的前景色与背景色
fg:    前景色
bg：背景色
'''
from tkinter import *

root = Tk()
bfg = Button(root, text='change foreground', fg='red')
bfg.pack()

bbg = Button(root, text='change backgroud', bg='blue')
bbg.pack()
root.mainloop()
