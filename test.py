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