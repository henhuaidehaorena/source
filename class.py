class Employee(object):
	#global empcount
	empcount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empcount=Employee.empcount+1#每初始化一个员工人数加1
	def displaycount(self):
		print('total employees are',Employee.empcount)
	def name_salary(self):
		print('%s:%d'%(self.name,self.salary))
##############################################
Chen=Employee('Chen',20000)
##############################################
Chen.displaycount()#创建第一个对象
Chen.name_salary()
Alex=Employee('Alex',20000)#创建第二个对象
Alex.displaycount()
Alex.name_salary()


###############################################
####Eric VS hashiqi
###hahsiqi进攻时，Eric可以选择进攻或防守，而Eric进攻时，hashiqi一直进攻
import os####为引用清屏做准备
import random####引入随机数模块
class Person:
	#def __init__(self,name,aggresivity,man_life_value):
####游戏功能扩充，由于人类打不过hashiqi，此时需要使用武器来增加战斗力和血量，
####而要求是需要花钱购买武器，因此需要对class Person重新定义
	#def __init__(self,name,aggresivity,man_life_value,money):
	#####需求变化：实例化对象攻击力随机，该如何实现？
	def __init__(self,name,man_life_value,money):
		self.name=name
		#self.aggresivity=random.randint(5,10)####
		#self.aggresivity=aggresivity
		self.man_life_value=man_life_value
		self.money=money#####为人类赋予金钱属性，有了钱可以用于购买武器
	##########初始化方法,定义属性
	def man_attack(self,dog):#人可以攻击狗，此时狗为一个对象
	#def man_attack(self)
		self.aggresivity=random.randint(0,10)##########类person的攻击力为5~10之间的随机数
		dog.dog_life_value=dog.dog_life_value-self.aggresivity  ###
		#dog_life_value=dog_life_value-self.aggresivity
		return dog.dog_life_value
	def man_being_attacked(self,dog):
		self.man_life_value=self.man_life_value-dog.aggresivity*0.5 ####person选择防守，失血量降为原来的50%
		####################由于人类无法战胜hashiqi,于是，接下来为人类赋予武器方法
class Dog:
	"""docstring for dog"""
	def __init__(self, name,aggresivity,dog_life_value):
		self.name=name
		self.aggresivity=aggresivity
		self.dog_life_value=dog_life_value

	def dog_bite(self,person):
		person.man_life_value=person.man_life_value-self.aggresivity
		return person.man_life_value
#######################设定武器类#######################################
class Weapon:
	def __init__(self,user_name,cost_money,weapon_aggresivity,weapon_HP_increase):
		self.user_name=user_name#######购买和使用武器的人
		self.cost_money=cost_money#####购买武器的花费
		self.weapon_aggresivity=weapon_aggresivity####武器的武力增值
		self.weapon_HP_increase=weapon_HP_increase######武器为使用者增加的血量
#####################################################
	#####设置武器的技能(方法)
	def weapon_buy_ability(self,person):#####为使用武器者增加技能和血量
		#person.aggresivity=person.aggresivity+self.weapon_aggresivity
		####使用者技能增加,购买后只能增加一次
		person.man_life_value=person.man_life_value+self.weapon_HP_increase
		###使用者血量增加，购买后只能增加一次
		person.money=person.money-self.cost_money
		#####购买武器要花费金钱，注意要判用户金钱是否大于武器单价，才确定能否购买
	def weapon_kaigua(self,dog):
		dog.dog_life_value=dog.dog_life_value-self.weapon_aggresivity
		#########武器购买之后，永久有效，因此技能永久有效
########################################################################
#实例化Person Eric和Dog hashiqi对象
os.system('cls')###windows下清屏
#os.system('clear')#####linux下清屏
Eric=Person('Eirc',100,100)####初始金钱设定为100
hashiqi=Dog('hashiqi',15,100)
dagougun=Weapon('Eric',50,5,10)##实例化武器打狗棍

if(Eric.money>=dagougun.cost_money):
		dagougun.weapon_buy_ability(Eric)####Eric购买了武器
print('Eric当前血量为:',Eric.man_life_value)
print('hashiqi当前血量为:', hashiqi.dog_life_value)######Eric的攻击力为随机数生成，取值5-10
print('以上为测试专用，用于验证变量是否正常工作\n')
##################################################
print('*'*10+'游戏加载中,请稍候~'+'*'*10)
#######################################################
while (Eric.man_life_value>0 and hashiqi.dog_life_value>0):
#只要双方血量均大于0，则游戏继续
###现在有hashiqi发起进攻
###先查看Eric和hashiqi的血量
	print('Eric当前血量为:',Eric.man_life_value)
	#print('Eirc当前攻击力为:',Eric.aggresivity)
	print('hashiqi当前血量为:', hashiqi.dog_life_value)
############################################################################################	
####设置if条件语句，增加游戏交互性
	attack_or_not=input('请Eric选择进攻还是防守("A/D"):')####玩家可选择攻击或防守，Eric一直进攻
	if(attack_or_not.upper()=='D'):####用户有可能输入非标准字符，如小写字母a/d,此处需要转换为大写
		print('hashiqi当前攻击力为',hashiqi.aggresivity)
		Eric.man_being_attacked(hashiqi) #hashiqi率先发起进攻,而Eric选择防守，此处没有调用hashiqi.dog_bite()函数
		if (Eric.man_life_value<=0):
			print('Eric当前血量为:',Eric.man_life_value)
			print('Eric Lost,Game over~')
			break #血量小于0，游戏结束，跳出循环
###########################################################################################
	elif(attack_or_not.upper()=='A'):####用户有可能输入非标准字符，如小写字母a/d,此处需要转换为大写
		Eric.man_attack(hashiqi)#Eric和hashiqi均开始进攻
		print('Eric当前攻击力为',Eric.aggresivity)
		dagougun.weapon_kaigua(hashiqi)######Eric开始使用武器打狗棍
		if hashiqi.dog_life_value<=0:
			print('hashiqi当前血量为:', hashiqi.dog_life_value)
			print('哈士奇Lost,Game over~')
			break #血量小于0，游戏结束，跳出循环
		hashiqi.dog_bite(Eric)#####hashiqi进攻函数
		if(Eric.man_life_value<=0):
			print('Eric当前血量为:',Eric.man_life_value)
			print('Eric Lost,Game over~')
			break #血量小于0，游戏结束，跳出循环
	else:
		print('*'*10+"Invalid input, please try again~"+'*'*10)
#此处出现变量man_life_value引用遭遇定义之前的报错，该如何解决
#############################################################################################
####游戏功能扩充：由于人类打不过hahiqi，此时需要使用武器来增加战斗力和血量，
####而要求是需要花钱购买武器，因此需要对class Person重新定义


			

