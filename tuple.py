###元组tuple的概念和列表类似，只不过元组和字符串一样是不可以被修改的
###元组通过小括号中的都好分割的项目定义
###被使用的元组的数值不会改变
zoo=('elephant','lion','tiger','dolphin')
print('the number of animals in the zoo is',len(zoo))
#print'the number of animals in the zoo is %d' %(len(zoo))
################print的两种表示方法，第一种使用逗号隔开，但是为什么此处会报错？
new_zoo=('wolf', 'penguin','zoo')
#此处zoo被人为是普通字符串，与wolf等地位相同
new_zoo_1=('wolf', 'penguin',zoo)
#此处zoo在另一个元组内，但是仍为元组
print(new_zoo)
print(new_zoo_1)
######此处比较new_zoo与new_zoo1的不同
print('number of animals in the new_zoo_1 is',len(new_zoo_1))
print('all animals brought from the old zoo is',new_zoo_1[2])
#此时元组zoo为新元组的一部分，但仍然保留元组的身份不变
print('the last animals brought from the old zoo is',new_zoo_1[2][3])

####################################################################
###含有0或者1个元素的元组该如何表示
###一个空的元组由元组名称和一对空的小括号组成，如name()
#然而，含有单个元素的元组相对较为复杂，
#必须在唯一的一个元素后面加逗号以示区分，
#如包含一个元素2的元组可以表示为name(2,)
#a=(1,2)
#b=(3)
#c=a+b
#print (c)
#报错如下：Traceback (most recent call last):
 # File "<interactive input>", line 28, in <module>
#TypeError: can only concatenate tuple (not "int") to tuple
#原来python解释器把(3)当作一个算数表达式来处理的，
#它的结果就是一个int型对象。为了和只有单个元素的元组区分，
#python规定要在元素后面带上一个逗号，例如d=(3,)。
#################
###元组中的元素值是不允许修改的，
#但我们可以对元组进行连接组合，如下实例:
a=(1,2)
b=(3,)
c=a+b
print (c)

#####使用元组输出
#
age=22
name='Alexander'
print('%s is %d years old'%(name,age))
print('why is %s so handsome? I can\'t believe it.' %(name))

