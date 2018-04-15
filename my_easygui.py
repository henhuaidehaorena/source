import easygui as g
import sys
import easygui as g

msg='请填写一下个人信息(其中带*的为必填项)'
title='账号注册系统'
fieldnames=['用户名','真实姓名','联系电话','QQ','Email']
fieldvalues=[]
fieldvalues=g.multenterbox(msg,title,fieldnames,fieldvalues)

print(fieldvalues)#用于查看返回的值是否赋给了fieldvalues
###############################################################################
while True:
	if fieldvalues == None :
		break
	errmsg = ""
	for i in range(len(fieldnames)):
		option = fieldnames[i].strip()
	if fieldvalues[i].strip() == "" and option[0] == "*":
		errmsg += ("【%s】为必填项   " %fieldNames[i])
	if errmsg == "":
		break
	fieldvalues = g.multenterbox(errmsg,title,fieldnames,fieldvalues)
	print("您填写的资料如下:%s" %str(fieldvalues))


########################################################
##passwordbox()
#passwordbox(msg='输入密码',title='',defalt='',image=None,root=None)
#passwordbox() 跟 enterbox() 样式一样，
#不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串：
my_password=g.passwordbox('请输入你的密码：')
print(my_password)

##########################################################
#######multpasswordbox()
##multpasswordbox(msg='',title='',fields=(),values=())
#multpasswordbox() 跟 multenterbox() 使用相同的接口，
#但当它显示的时候，最后一个输入框显示为密码的形式（"*"）：
msg='请输入用户名和密码'
title='用户登录系统'
user_info=[]
user_info= g.multpasswordbox(msg,title,('用户名','密码'))
print(user_info)

########################################################
##passwordbox()
#passwordbox(msg='输入密码',title='',defalt='',image=None,root=None)
#passwordbox() 跟 enterbox() 样式一样，
#不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串：
my_password=g.passwordbox('请输入你的密码：')
print(my_password)

##########################################################
#######multpasswordbox()
##multpasswordbox(msg='',title='',fields=(),values=())
#multpasswordbox() 跟 multenterbox() 使用相同的接口，
#但当它显示的时候，最后一个输入框显示为密码的形式（"*"）：
msg='请输入用户名和密码'
title='用户登录系统'
user_info=[]
user_info= g.multpasswordbox(msg,title,('用户名','密码'))
print(user_info)

while 1:
	g.msgbox("hi，欢迎进入第一个界面小游戏，haha~")
	msg="你希望在致力学习到什么知识呢？"
	title="小游戏互动"
	choices=["谈恋爱","编程","琴棋书画","人际关系"]
	choice=g.choicebox(msg,title,choices)
	g.msgbox("你的选择是："+str(choice),"结果")
	msg="你希望重新开始小游戏吗？"
	title="请选择"
	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)

	#easygui的各种功能演示
	#从IDE上来调用：
	#import easygui as g
	#g.egdemo
	#####################################
	#导入easygui
	#import easygui
	#如果使用这种方式进行导入，
	#那么在引用easygui的时候需要使用类似easygui.msgbox()
	#第二种选择是导入整个easygui包：
	#from easygui import *
	#这时我们可以更容易调用easygui函数，
	#可以这样编写代码 msgbox()
	#第三种选择是类似下面这种语句：
	#import easygui as g
	#这样可以保持easygui的命名空间，同事避免重复输入此函数
	#g.msgbox()
	###########################################################
	##使用easygui
	#一旦模块中导入easygui，则GUI操作就变成了调用easygui函数的操作了
	import  easygui as g
	g.msgbox("Hello world again~")
	################################################################
	#easygui函数的默认参数
	#对于easygui中的所有的函数而言，前两个参数分别是消息和标题
	#大部分的easygui函数都有默认参数，
	#比如msgbox()函数的标题部分就是可选的，所以在调用msgbox()是可以只指定一个消息参数


import easygui as g
msg='请填写一下个人信息(其中带*的为必填项)'
title='账号注册系统'
fieldnames=['用户名','真实姓名','联系电话','QQ','Email']
fieldvalues=[]
fieldvalues=g.multenterbox(msg,title,fieldnames,fieldvalues)








