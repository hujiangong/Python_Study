from tkinter import Tk
from tkinter import Label
from tkinter import Button
import tkinter.filedialog

# root1 = Tk()
#
# def openfile():
#     """
#     打开一个文件我们将使用的对话函数是askopenfilename()
#     :return:
#     """
#     filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb1.config(text="您选择的文件是：" + filename)
#     else:
#         lb1.config(text="您没有选择任何文件")
#
# lb1 = Label(root1, text='')
# lb1.pack()
# btn1 = Button(root1, text="弹出选择文件对话框", command=openfile)
# btn1.pack()
# root1.mainloop()

# root2 = Tk()
# def openfiles():
#     """
#     打开多个文件用askopenfilenames()
#     tkinter.filedialog.askopenfilenames()返回的是一个tuple数据类型
#     :return:
#     """
#     filenames = tkinter.filedialog.askopenfilenames()
#     if len(filenames) != 0:
#         string_filename = ""
#         for i in range(0, len(filenames)):
#             string_filename += str(filenames[i]) + "\n"
#         lb2.config(text="您选择的文件是：" + string_filename)
#     else:
#         lb2.config(text="您没有选择任何文件")
#
# lb2 = Label(root2, text='')
# lb2.pack()
# btn2 = Button(root2, text="弹出选择文件对话框", command=openfiles)
# btn2.pack()
# root2.mainloop()

root3 = Tk()
root3.geometry('350x150')
driname=''
def opendir():
    """
    打开文件夹用askdirectory()
    :return:
    """
    # filenames = tkinter.filedialog.askopenfilenames()
    driname = tkinter.filedialog.askdirectory()
    if driname != '':
        lb3.config(text="您选择的目录是：" + driname)
    else:
        lb3.config(text="您没有选择任何目录")

lb3 = Label(root3, text='')
lb3.pack()
btn3 = Button(root3, text="弹出选择目录对话框", command=opendir)
btn3.pack()
root3.mainloop()
print('driname'+driname)
# dirname = tkinter.filedialog.askdirectory()
# print(dirname)