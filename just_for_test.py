import time
import datetime
###datetiem模块
s='1234'
print(s.isdigit())#isdigit()用于判断是否为字符串,条件为真，返回True
q='1234abcd'
print(q.isdigit())#isdigit()用于判断用户的输入是否为数字，如果确实是数字，则需要s进一步使用int()转换为数字

age_check=0


##年龄输出
print('*'*10+'好牛鼻啊'+'*'*10)
while not age_check:
	age=input('请输入您的年龄>>>')
	print(age)#调试使用
	if age.isdigit():#只有当用户正确输入数字时，才进行字符到整形数据的转换
		age=int(age)
		age_check=1#正确输入，不再要求重复输入
	else:
		print('wrong input, please input digit again')

#################time延时函数
time.sleep(1)
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
while 0:
	print(datetime.datetime.now())
	time.sleep(5)
	print(datetime.datetime.now().date())
	time.sleep(5)
	print(datetime.datetime.now().time())
	time.sleep(5)
#########################################
#如何计算时间间隔
###############################

grade=[100,90,'lilei',100,100]
print(grade)
grade.append('打游戏刚获得的装备')
print(grade)
##判断某个元素是否存在于列表中， in
##判断玩家是否有某件装备
if '解药'in grade:
	print('yes')
else:
	print('no')
############################################
#删除列表元素
#用del 列表元素
del grade[0]
print(grade)
#####获取列表长度 len()
####如果游戏玩家装备数量达到上限，禁止再往背包中增加装备
print(len(grade))

#查询列表中某个元素重复的次数
#用列表.count(要查询的元素)来获取
print(grade.count(100))

#查询列表中某个元素第一次出现的位置
#使用列表.index(元素名称)来获取
print(grade.index('lilei'))


















