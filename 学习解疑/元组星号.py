# *号相当于将元组解包
list =(0,1,2,3,4,5)
print(list)
print(*list)
def sumList(*s):
    print(s)
sumList(list)

# 在字典中相当于取键值
list={'a':1,'b':2}
print(list)
print(*list)
