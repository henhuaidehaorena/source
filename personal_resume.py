#makerbean游戏开发课程
#第一节 创建交互式个人简历
name=input('请输入您的姓名：')
xingbie=input('请输入您的性别：')
while (xingbie!=('男') and xingbie!=('女')):
	#xingbie!=('男'or'女'):错误表达方式
	#此处存在bug,如输入为”女“,条件仍然成立，仍然会进入循环
	print('性别错误，please try again!\n')
	xingbie=input('请输入您的性别：')
age=int(input('请输入您的年龄：'))
#input函数默认返回字符型数据
school=input('请输入您的学校名称：')
print('正在生成您的简历，请稍后\n')
print('\n')
print('*'*20)#*号重复输出20次
##等效于print('*******************************************')
print('					简历')
print('\n')
print('''
	姓名：%s\n
	性别：%s\n
	年龄：%d\n
	学校：%s\n''' %(name,xingbie,age,school))

##format格式化输出
s="{} {}".format('hello','world')
print(s)

#######################################################
####and or not
###range()函数可以得到一个整数序列
#for i in range(2,10,2)
#		print(i)

###########################################
#while 1:
	#pass#pass语句，即此行什么都不做
	#print("hello")



###关于标记变量
checksex=False   #输入错误时，一直指导用户重新输入
while not checksex:
	sex=input('请输入你的性别(F/M):>>>')
	if sex.upper()=='F':
		print("你是女生")
		checksex=True  #checksex值为True,即not True为false，不满足条件，跳出循环
	elif sex.upper()=='M':
		print('你是男生')
		checksex=True   #checksex值为True,即not True为false，不满足条件，跳出循环
	else:
		print('不支持的字符，请再次输入(F\M)')

#s.isdigit()
