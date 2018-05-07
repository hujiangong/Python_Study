import sys
print(sys.path)
'''
输出当前工作目录
['D:\\学习\\Python\\workspace-64bit\\学习解疑', 'D:\\学习\\Python\\workspace-64bit', 'D:\\Program Files (x86)\\Python\\Python36\\python36.zip',
'D:\\Program Files (x86)\\Python\\Python36\\DLLs', 'D:\\Program Files (x86)\\Python\\Python36\\lib', 'D:\\Program Files (x86)\\Python\\Python36',
'D:\\Program Files (x86)\\Python\\Python36\\lib\\site-packages']
'''

# import导入时，如果路径中出现了空格，没有办法，只能删除空格!!
# 好吧，如果实在要使用的话，可以用 __import__() 函数，不建议使用。这个函数用于动态加载类和函数 。

# 在PyCharm中sys.path的变量和在cmd中的sys.path的变量是不一样的。
# 所以在cmd中可能会出现import失败的情况。
# 可以在"PYTHONPATH"的系统环境中增加你需要的路径