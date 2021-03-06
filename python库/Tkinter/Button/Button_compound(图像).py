'''3.与Label一样，Button也可以同时显示文本与图像，使用属性compound'''
from tkinter import *

root = Tk()
# 图像居下,居上，居右，居左，文字位于图像之上
Button(root, text='botton', compound='bottom', bitmap='error').pack()
Button(root, text='top', compound='top', bitmap='error').pack()
Button(root, text='right', compound='right', bitmap='error').pack()
Button(root, text='left', compound='left', bitmap='error').pack()
Button(root, text='center', compound='center', bitmap='error').pack()
# 消息循环
root.mainloop()

''''' 
Button显示图像 
image:可以使用gif图像，图像的加载方法img = PhotoImage(root,file = filepath 
bitmap:使用X11 格式的bitmap,Windows的Bitmap没法显示的，在Windows下使用GIMP2.4将windows 
Bitmap转换为xbm文件，依旧无法使用.linux下的X11 bitmap编辑器生成的bitmap还没有测试，但可 
以使用内置的位图。 
(1).使用位图文件 
bp = BitmapImage(file = "c:/python2.xbm") 
Button(root,bitmap = bp).pack() 
(2).使用位图数据 
BITMAP = """ 
#define im_width 32 
#define im_height 32 
static char im_bits[] = { 
0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f, 
0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b, 
0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05, 
0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93, 
0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3, 
0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3, 
0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a, 
0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed, 
0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d, 
0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6, 
0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe, 
0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd, 
0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba, 
0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b, 
0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59, 
0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa 
}; 
""" 
使用tuple数据来创建图像 
bmp = BitmapImage(data = BITMAP) 
Button(root,bitmap = bmp) 
'''
