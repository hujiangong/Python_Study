from tkinter import *

def counter():
    global count
    a = count
    i = int(a)
    i += 1
    a = str(i)
    count = a
    botton['text'] = count
    # botton.config(text=a)

window = Tk()
frame = Frame(window)
frame.pack()
# global count
count = StringVar()
count = '0'
botton = Button(frame, text=count, command=counter)
botton.pack()

window.mainloop()
