###########################################################
##python之列表生成式、生成器可迭代对象与迭代器
#列表生成式
#生成器（Generator）
#可迭代对象（Iterable）
#迭代器（Iterator）
#Iterable、Iterator与Generator之间的关系
###########################################################
##列表生成式：用于生成一个我们想要的列表
#语法格式：[exp_1 for iter_var in iterable if exp_2]
#说明：exp_1为我们想要生成的列表格式，即目标列表
#iter_var为变量，其会依次遍历源列表中的数值，iterable为源列表，
#if exp_2为筛选的条件，因为有些列表中的数值不是我们想要的，
#可以通过if语句将其删除

#其工作过程类似如下所示：
#L=[]   #建立一个空的列表
#for iter_var in iterable:
	#if exp_2:判断是否满足条件
#		L.append(exp_1)#将满足条件的新元素依次追加到目标列表的尾部
###############################################################
###循环嵌套语法格式：
#[exp_1 for iter_var_A in iterable_A for iter_var_B in iterable_B if expe_2]
#相当于每迭代一个iterable_A中的元素，就把iterable_B中的所有元素都迭代一遍
#L=[]
#for iter_var_A in iterable_A:
	#for iter_var_B in iterable_B:
		#L.append(exp_1)
################################################################
#####应用场景
##生成一个2n+1的数字列表，n为从3到10的数字
list_example=[2*n+1 for n in range(3,11) ]
print(list_example)
###过滤出一个指定的数字列表中数值大于20的元素
LQ= [3,7,11,14,19,33,26,57,99]
LA=[n for n in LQ if n>20]
print(LA)
###计算两个元素的全排列，并将结果保存至一个新的列表中
L1=['香蕉', '苹果', '橙子']
L2=['可乐', '牛奶']
list_2=[(x,y) for x in L1 for y in L2]
print(list_2)
list_1=[x+y for x in L1 for y in L2]
print(list_1)
#######注意以上两个生成的列表时不同的

###将列表中的元素全部改为小写，列表元素为字符串的保留，不是的则删除
#同时利用isinstance()排除无法进行小写操作的数字
##################################################################
# -*- coding: utf-8 -*-
L3 = ['Hello', 'World', 18, 'Apple', None]

L4=[s.lower() for s in L3 if isinstance(s,str)]
print(L4)
if (L4==['hello','world','apple']):
	print('测试pass!')
else:
	print('测试fail!')

#Python 中的isinstance函数，isinstance是Python中的一个内建函数。是用来判断一个对象的变量类型。
#以下是 isinstance() 方法的语法:
#isinstance(object, classinfo)
#参数
#object -- 实例对象。
#classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
#返回值
#如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False

###########把一个列表中所有的字符串转换成小写，非字符串元素原样保留
L5 = ['Hello', 'World', 18, 'Apple', None]
L6=[s.lower() if isinstance(s,str) else s for s in L5  ]
####谁能告诉我，为什么语法变成了这样？不能参照下面的写法吗？
#L6=[s.lower() for s in L3 if isinstance(s,str) else s for s in L3]
print('L6 is',L6)
##################################################################
####将一个字典转换为由一组元祖组成的列表，元组格式为(key,value)
D = {'Tom': 15, 'Jerry': 18, 'Peter': 13}
new=[(key,value) for key,value in D.items() ]
print(new)
#####字典的访问与列表不同，比如字典在同时迭代key和value时
####需要使用dict的items()方法

