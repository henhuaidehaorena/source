import easygui  as g
import sys
#easygui函数的默认参数
	#对于easygui中的所有的函数而言，前两个参数分别是消息和标题
	#大部分的easygui函数都有默认参数，
	#比如msgbox()函数的标题部分就是可选的，所以在调用msgbox()是可以只指定一个消息参数
#g.msgbox("i love you, alex")
##当然在调用时亦可以指定全部参数，如：
#g.msgbox("I love you,alex",'fans note')
#在各类按钮组件里，默认的参数是"shall I continue?"，所以我们可以不带任何参数的去调用ccbox()
#当选择cancel或者关闭窗口是返回一个布尔类型的值

###########################################################################################
#msgbox()
##################
g.msgbox(msg="终于学到图形界面了，太牛逼了",title='真TM爽',
	ok_button="走起，走起",image=None,root=None)
##########################################################
#ccbox()
####################
g.ccbox(msg="再多来一个小时",title="坚持就是胜利",
	choices=("continue","cancel"),image=None)
##ccbox()提供一个选择，continue或者cancel，
#并根据选择的是continue还是cancel相应返回1或者0；
#########################################################
#if ccbox(): 
 #   pass         # user chose to continue
#else: 
 #   return      # user chose to cancel
########################################################
if g.ccbox("要再来一发吗？","再来一发否",
	choices=("好啊，好啊","算了吧")):
	g.msgbox("不要走，决战到天亮~")
else:
	sys.exit(0)###注意此处先import sys
############################################################
####ynbox()
##ynbox()与ccbox功能类似
################################
######buttonbox()
fruit=g.buttonbox(msg='你喜欢哪种水果啊',title='水果传说',
	choices=('apple','pine apple','watermelon','strawberry'),image=None)
#可以使用 buttonbox() 定义自己的一组按钮，buttonbox() 会显示一组你定义好的按钮。
if (fruit=="apple"):
	print("Wow, i love apple too")
elif(fruit=="pine apple"):
	print("It is too sour~")
elif(fruit=="watermelon"):
	print("It is so sweet~")
elif(fruit=="strawberry"):
	print("It is the best~")
print('I like fruit')

#当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。
#如果用户取消或者关闭窗口，那么会返回默认选项（第一个选项）。
#请看例子：
###########################################
#如何在buttonbox函数(magbox/ynbox等等)里显示显示图片
#你还可以为关键字参数 image 赋值，
#这是设置一个 .gif 格式的图像（注意仅支持 GIF 格式）：
g.buttonbox(msg='alex长得帅不帅',title='Handsome man',
	choices=('帅','很帅','帅到掉渣'),image='demo.gif')
#################################################################
#####choicebox()
#语法格式：choice(msg='',title='',choices=())

choice=["有钱的时候愿意","愿意","不愿意"]
reply=g.choicebox(msg="你愿意付费购买吗?",title='知识有偿获取',choices=choice)
#按钮组件方便提供用户一个简单的按钮选项，
#但如果有很多选项，或者选项的内容特别长的话，更好的策略是为它们提供一个可选择的列表。
#choicebox() 为用户提供了一个可选择的列表，使用序列（元祖或列表）作为选项，
#这些选项显示前会按照不区分大小写的方法排好序。  
############################################################################
##multichoicebox()
#
import easygui as g
g.multchoicebox(msg='尽量选取多的项目',title='多项选择，不要犹豫哦~',
	choices=('西瓜','香蕉','苹果','梨子'))
#multchoicebox() 函数也是提供一个可选择的列表，
#与 choicebox() 不同的是，multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。 
#multchoicebox() 函数也是使用序列（元祖或列表）作为选项，
#这些选项显示前会按照不区分大小写的方法排好序。
#############################################

#####enterbox()
#enterbox()为用户提供一个简单的输入框，返回值为用户输入的字符串
#默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。
#enterbox(msg='enter here',title='',default='',strip=True,image=None,root=None)
my_inner_word=g.enterbox(msg='我们简单聊聊呗',title='爱传万家，说出你的故事')
print(my_inner_word)
#########################################################################

###interbox()
####interbox(msg='',title='',default='',lowerbound=0, upperbound=100,image=None)
#interbox()为用户提供一个简单的输入框，
#用户只能输入范围内的整形数值，否则会要求重新输入
import easygui as g
score=g.interbox(msg='请输入你的得分',title='分数统计系统',
	lowerbound=0, upperbound=100)
##################################################
if(score>=60):
	print('congratulations, you passed the exam')
else:
	print('sorry, you need to test again')
##################################################################
##*****************************************************************************
#####multenterbox()
#multenterbox(msg='Fill in the values for the blanks',title='',fields=(),values=())
###请注意一下内容：
#如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
#如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
#如果用户取消操作，则返回域中的列表的值或者None值
###############################################################
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
