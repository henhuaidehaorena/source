####面向对象编程OOP
##继承
#在开发程序的过程中，如果我们定义了一个类A，然后又想新建立另外一个类B，
#但是类B的大部分内容与类A的相同时
#我们不可能从头开始写一个类B，这就用到了类的继承的概念。
#通过继承的方式新建类B，让B继承A，
#B会复制A的所有属性(数据属性和函数属性)，实现代码重用
#继承是一种创建新类的方式，
#在python中，新建的类可以继承一个或多个父类（基类），
#新建的类称为派生类或者子类；python中类的继承分为：单继承和多继承；

class Parentclass1:#定义父类
	pass
class Parentclass2:#定义父类
	pass
class Subclass1(Parentclass1):
#单继承，父类是Parentclass1,子类是Parentclass2
	pass
class Subclass2(Parentclass1,Parentclass2):
#多继承，用逗号分隔开多个继承的类
	pass
class Subclass3:####没有指定父类名称
	pass
#######################################
#####查看继承：
##子类名称.__base__ or 子类名称.__bases__
jicheng_1=Subclass1.__bases__##__base__只查看从左到右继承的第一个父类
print(jicheng_1)
jicheng_2=Subclass2.__bases__####__bases__则查看继承的所有的父类
jicheng_3=Subclass2.__base__
print(jicheng_2)
print(jicheng_3)
print(Subclass3.__base__)
###如果在定义类中没有指定父类，则默认为object，object是所有python类的父类

class Animal:####定义父类
	def __init__(self,name,aggressivity,life_value):
		self.name=name
		self.aggressivity=aggressivity
		self.life_value=life_value

	def eat(self):
		print("%s is eating" %self.name)

class Dog(Animal):###定义子类（派生类），派生于Animal
	def __init__(self,name,pinzhong,aggressivity,life_value):
	########################################################
		#super().__init__(name,aggressivity,life_value)
		#此处使用到了super()类来进行初始化父类的init方法，
		#由于super()通常使用在多继承中，因此此处不推荐使用，
		##现在使用父类名称.func(self)来调用父类的函数
		Animal.__init__(self,name,aggressivity,life_value)
	####调用父类的init方法，注意此时的init中不带self参数####################################
		self.pinzhong=pinzhong###派生出pinzhong属性

	def bite(self, people):
		pass###派生出咬人的技能(函数)
	def eat(self):
		Animal.eat(self)
		#super().eat()###这两者之间有什么区别
class Person(Animal):
	def __init__(self,name,aggressivity,life_value,money):
		Animal.__init__(self,name,aggressivity,life_value)
		self.money=money####派生出金钱属性，用于购买武器
	def attack(self,dog):
		pass##派生于打钩技能
	def eat(self):
		super().eat()
##############################################################
hashiqi=Dog('hashiqi',"哈士奇",10,100)
Eric=Person('Eir',8,80,50)###初始化实例
############################################################
hashiqi.eat()
print(hashiqi.pinzhong)
Eric.eat()
print(Eric.money)


def funA(arg):
    print ('A')
    a=arg()

@funA
def funB():
    print('B')


#####递归函数调用
def digui_func(n):
	if (n==1):
		return 1
	else:
		return digui_func(n-1)*n
print(digui_func(10))


#####汉诺塔问题,递归函数
def move(n,a,b,c):
	if(n==1):
		print(a,"--->",c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(5,'A','B','C')


a=[2,1,5,4,3,6,0]#输入一个数组
a.sort()
print(a)
tuple_1=(max(a),min(a))
print(tuple_1)

