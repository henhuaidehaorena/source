#####
class student(object):#定义student类
	"""docstring for student"""
	def __init__(self,name, score):
		#_init_方法(函数)第一个参数 永远是self,表示创建的实例本身
		#因此在_init_内部，可以把各种属性绑定到self，因为self就指向创建的实例本身。
		self.name=name #student的属性
		self.score=score
	def print_score(self):#方法，即函数
		print('name:%s score:%d' %(self.name,self.score))

	####此处还可以继续定义新的方法，增加了扩展型
	def get_rank(self):
		if self.score>80:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'


Alex=student("Alex",100)#创建对象实例，对象是通过类名+()实现的，
#相当调用于_init_方法
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
#但self不需要传，Python解释器自己会把实例变量传进去：
Chen=student("Chen",50)#给对象Alex和Chen设定属性
Alex.print_score()
print("Alex's rank is %s" %Alex.get_rank())
Chen.print_score()
print("Chen's rank is %s" %Chen.get_rank())

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
#面向对象最重要的就是类和对象(实例)，
#类是抽象的模板，而对象(实例)是根据类创建出来的一个个具体的对象
#每个对象都拥有相同的方法(函数)

#########总结
#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

#通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
##################03.26
#对象=属性+方法
#OOP的特征：封装+继承+多态
#Class Mylist(list):#Mylist类继承了list的属性和方法
	#pass

####公有和私有
##在python中，对象的属性和方法是公有的
#在python中定义私有变量只需要在变量名或函数名前加上"__"两个下划线，那么这个变量或者函数就会变成私有的了
#私有变量如何引用？