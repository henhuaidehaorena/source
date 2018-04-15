################################
print('\\\n\\')
print('i\'m learning \npython')
print('''i'm learning python''')
print('\\\t\\')
print('''\\\t\\''')
print('\\\\t\\')
print('''\\\\t\\''')
############################################

print('line1\nline2\nline3')
print('pls input your number:\n')
value=input()
print('value=',value)
print(1>2)
a=1 #A是整型变量
print(a);
a='char list' #a是字符串 字符变量
print(a);


###########################################################################
#if sentence
print('pls input your age:')
age=input()
age=int(age)
if(age>=18):
	print('you are adult, your age is %d' %(age))	
	print(age)
elif(age>=6):
	print('you are teenager, your age is %d' %(age))	
	
else:
	print('you\'re kid,your age is %d' %(age))
	
#####################################################################
#elif是else if的缩写，if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
#把该判断对应的语句执行后，就忽略掉剩下的elif和else；

################################################################
#再议input函数
#再议 input

#最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：

#age=input()
#if(age>=18):
#	print('you are adult, your age is:')	
#	print(age)
#elif(age>=6):
#	print('you are teenager, your age is:')	
#	print(age)
#else:
#	print('you\'re kid')
#	print(age)
#Traceback (most recent call last):
 # File "transfer.py", line 21, in <module>
  #  if(age>=18):
#TypeError: '>=' not supported between instances of 'str' and 'int'
#这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
################################################################################################################################


height=1.75
weight=80.5
bmi =weight/(height*height)
print('your bmi is:%.2f,' %(bmi))
#此处描写了如何输出带有小数点的数据
if(bmi<18.5):
	print('too light')
elif(bmi<25):
	print('normal')
elif(bmi<28):
	print('too heavy')
elif(bmi<32):
	print('too fat')
else:
	print('very fat')


#for 循环语句
#1 for...in循环 
print('for循环语句实例\n')
names=['Michael','Alexander','Yolo']
for name in names:
	print(name)
#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
#再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	#此处用数组形式该如何表达？
	sum=sum + x
print(sum)

#如果要计算1-100的整数之和，从1写到100有点困难，
#幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
#比如range(5)生成的序列是从0开始小于5的整数：

qiuhe=0;
for i in range(101):
	qiuhe=qiuhe+i
print(qiuhe)
#相邻的两个语句具有相同的缩进，意味着他们在同一个循环里面；

yushu_qiuhe=0
for j in range(100):
	if(j%2==1):
		yushu_qiuhe=yushu_qiuhe+j
print(yushu_qiuhe)	

#while循环
m=0
n=1
while (n<=99):
	m=m+n
	n=n+2
print(m)
print(n)


L=['Bart','Lisa','Adam']
for firstname in L:
	print('Hello,%s' %firstname)
		 #为什么不能写成 print('Hello,%s!', %(xingming))
#SyntaxError: unexpected EOF while parsing  
#EOF问题该如何解决
###对于EOF问题，通常是由于直接复制代码产生的缩进问题，
###可以重新输入部分复制粘贴的代码
