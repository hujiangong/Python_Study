# 作者：田田田田
# 链接：https://www.zhihu.com/question/58829932/answer/279415873
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from tkinter import *

#在函数之外定义一个全局可用的变量，用于在mainloop之后返回。
#它的值在函数中也可以修改，声明global
#这个问题的关键在于：要从python语法方面想问题
# 在语法层面，root、lb是实例，def ok()是函数，它们是平级的。lb.curselection()看起来是执行lb的方法，照理说在这个平级的位置是可以用的（既然lb.pack()能用为什么lb.curselection()不能用？
# 但实际结果是：lb.curselection()比较特殊，只有在command=ok的ok函数内部才可以用感觉大概是因为lb.curselection()调用依赖于command提供的上下文。
#既然ok函数的返回确实拿不到，我们又需要把ok内部的值往外传递，那可以换一种思路：让ok函数直接修改外面的变量。具体实现就是在函数外定义一个变量，然后在函数中声明为global
seq_selected=0


root = Tk()

lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.pack()

def ok():
	var1=lb.get(lb.curselection())
	global seq_selected
	seq_selected=var1
	root.destroy()
button = Button(root, text="提交", command=ok)
button.pack(side=RIGHT)
#print(lb.get(lb.curselection()))#报错
#root.wait_window(lb)
root.mainloop()
print(seq_selected)

# 如果要把上述代码全部装进一个函数，那么需要特别注意：seq_selected需要放在函数外。
# 封装后的代码如下：

seq_selected=0
#这一句一定要在外面，不然在users_choice的返回还是0，作用域问题？
def users_choice():
	print('sss')
	root = Tk()
	lb = Listbox(root)
	for i in range(10):
		lb.insert(END,str(i))
	lb.pack()

	def ok():
		var1=lb.get(lb.curselection())
		global seq_selected
		seq_selected=var1
		root.destroy()
	button = Button(root, text="提交", command=ok)
	button.pack(side=RIGHT)
	#print(lb.get(lb.curselection()))#报错
	#root.wait_window(lb)
	root.mainloop()
	return (seq_selected)

if __name__=='__main__':
	print(users_choice())
	print(seq_selected)
#因为seq_selected变量和users_choice()函数平级
#这时可以理解为：users_choice()修改了一个它外部的变量，所以users_choice()甚至可以没有返回
#直接打印该变量这个外部变量即可