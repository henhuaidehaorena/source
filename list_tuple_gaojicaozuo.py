#取一个list或者tuple的部分元素师非常常见的操作。
#一个常见的list如下所示：
L=['Michael','Sarah','Tracy','Bob','Jack']
#提出问题，如何取出列表L的前三个元素？
#笨办法：
r=[]#建立一个空的列表
n=3
for i in range(n):
	r.append(L[i])#将L[]中的元素一次追加到r[]列表的末尾
	print(r)#查看r中的数据追加情况
print(r)#查看最终结果

#python切片操作符(slice)实现上述功能
new=L[0:3]
#L[0:3]表示从索引0开始取，直到索引3之前位置，即索引0,1,2
print(new)
#也可以从索引1开始，取出2个元素出来：
new_2=L[1:3]
print(new_2)
#python同样支持倒数切片.倒数第一个元素的索引为-1
new_3=L[-2:-1]#不包含倒数第一个
print(new_3)
new_4=L[-2:]#从倒数第二至倒数第一索引
print(new_4)
#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串：


#####################################################################################################
def trim_joke(char_serial_input):####此函数只能去除行首行未的单个空格
	char_list=char_serial_input
	#char_list=input('请输入字符串:')
	###极端情况，输入字符串只有空格该如何处理？
	print('输入的字符串的长度为:',len(char_list))
	if(char_list[0]==' '):
		if(char_list[len(char_list)-1]==' '):##行首行尾均有空格
			char_list=char_list[1:-1]
			print('获得的新字符串为:',char_list)
			print('获得的新字符串长度为:',len(char_list))#查看新字符串的长度
		else:###行首有空格，行尾没有
			char_list=char_list[1:]
			print('获得的新字符串为:',char_list)
			print('获得的新字符串长度为:',len(char_list))#c产看新字符串的长度
	else:#行首无空格
		if(char_list[len(char_list)-1]==' '):##行尾有空格
			char_list=char_list[0:-1]
			print('获得的新字符串为:',char_list)
			print('获得的新字符串长度为:',len(char_list))#查看新字符串的长度
		else:###行首行尾均没有空格
			pass###不做切片处理
			print('获得的新字符串为:',char_list)
			print('获得的新字符串长度为:',len(char_list))#查看看新字符串的长度
	return char_list
print(trim_joke('123 '))
#####################################################################################
###再次抽象,可以去除所有的空格
#总体思想：先去除行首的空格，再取出行尾的空格
def trim_effective(char_list_s):
	char_list=char_list_s
	#if(char_list_s[0]==' '):#此处如果使用if 语句，不具备循环判断的功能，无法判断行首具有多个空格的情况，因该改为while
	while(char_list[0]==' '):
	##只要char_list_s[0]为空格，则条件为真，循环继续
		char_list=char_list[1:]
##############################################################
	while(char_list_s[-1]==' '):
		char_list=char_list[0:-1]
	return char_list###函数执行完毕，返回最终处理完毕的字符串
#####################################################################################################
######现在开始进行程序测试：
print(trim_effective('hello  '))
print(trim_effective('  hello  '))
print(trim_effective('hello'))
print(trim_effective(' hello ,world  '))

if trim_effective('hello  ') != 'hello':
    print('测试失败!')
elif trim_effective('  hello') != 'hello':
    print('测试失败!')
elif trim_effective('  hello  ') != 'hello':
    print('测试失败!')
elif trim_effective('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim_effective('') != '':
    print('测试失败!')
elif trim_effective('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
######################################################################################################################################################
####下面是我自己最开始编写的程序，事实上，该语法为顺序执行，无论输入的字符串是什么形式，在经过slice之后，最后一个条件语句总是符合的，因此会一直执行
#1.要求能够读取输入的字符串的长度 
#char_list=input('请输入字符串:')
#if(char_list[0]==' 'and char_list[len(char_list)-1]==' '):
#	char_list=char_list[1:-1]#行首行尾均有空格
#	print(char_list)
#	print(len(char_list))#c产看新字符串的长度
#if(char_list[0]==' 'and char_list[len(char_list)-1]!=' '):
#	char_list=char_list[1:]#行首有空格
#	print(char_list)
#	print(len(char_list))#c产看新字符串的长度
#if(char_list[0]!=' 'and char_list[len(char_list)-1]==' '):
#	char_list=char_list[0:-1]#行尾有空格
#	print(char_list)
#	print(len(char_list))#c产看新字符串的长度
#if(char_list[0]!=' 'and char_list[len(char_list)-1]!=' '):
#	pass#行首行尾均没有空格
#	print(char_list)
#	print(len(char_list))#查看新字符串的长度
