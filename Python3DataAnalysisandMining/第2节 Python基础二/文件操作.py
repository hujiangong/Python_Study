#open(filename,mode)打开文件  第一个参数文件路径+文件名，
# 第二个参数r只读
# r+ 可读可写，不会创建不存在的文件，从顶部开始覆盖写，不一定会全部覆盖
# w+ 可读可写 如果文件存在，则覆盖整个文件，不存在则创建
# w 只能写 覆盖整个文件 不存在则创建
# a 只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
# encoding指定写入的文件编码
file1=open("d:/file1.txt","w",encoding='utf-8')
#write(str[,]) 返回写入的长度
file1.write("我买几个橘子去。你就在此地，不要走动。")
file1.close()
file1=open("d:/file1.txt","r")
#data1=file1.read()

#readline()按行输出
#data1=file1.readline()
while True:
    line=file1.readline()
    if len(line)==0:
        break
    print(line)
#print(data1)
file1.close()