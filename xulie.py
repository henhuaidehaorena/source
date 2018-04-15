#python中常见的序列包括字符串，列表和元组。
#所谓序列，即成员的有序排列，可以通过下表进行访问；
#序列中的元素都是有序的，拥有自己的编号，从且0开始，
#可以通过索引得到序列中对应的元素
#索引也可以为复制，附属索引表示从右往左开始计数，
#最后一个元素索引为为-1，倒数第二个为-2，一以此类推

##############################################################
#所有序列都可以进行如下操作：
#索引
#分片
#加
#乘
#检查某个元素是否属于序列成员（成员资格）
##############################################################

##########################
###案例如下：
shoplist=['apple','pineapple','carrot','banana']
print('item o is', shoplist[0])
print('item 1 is', shoplist[1])
print('item 2 is', shoplist[2])
print('item 3 is', shoplist[3])
print('itme -1 is', shoplist[-1])
print('item -2 is',shoplist[-2])
print('item 0 to 2 is',shoplist[0:3])
print('item 2 to end is',shoplist[2:])
print('item begining to end is',shoplist[:])
print('last to begining is',shoplist[-1::-1])
print('item last to begining is',shoplist[::-1])
print('last to the daoshudierge is',shoplist[-1:-2])
#正向切片中冒号左边索引对应的元素晚于右边索引对应元素出现时,返回结果是[]
print('last to the daoshudierge is',shoplist[-1:-3:-1])
########################################################
########切片
#################################################
###使用索引可以获取单个元素，使用切片可以获取指定范围内的元素，
################################################################################################
#切片操作符是序列名后跟一个方括号，方括号中有一堆可选的数字，并用冒号分割
#简化为：obj[start_index:end_index]或者obj[:]
#表示获取从start_index开始到end_index-1(结束索引之前一位)结束所有索引对应的元素
#而obj[:]表示获取所有的元素
#obj[start_inedx:]表示从开始索引以及后面所有的元素
#obj[:end_index] 表示获取从0开始到end_index-1结束所有索引对应的元素　
#切片中冒号左边索引对应的元素晚于右边索引对应元素出现时,返回结果是[]
######################################################################################################
#[start_index:end_index:step] (step>0)表示从start_index索引对应的元素开始每step个元素取出来一个，
#直到取到end_index对应的元素结束(step默认为1)
#[start_index:end_index:step] (step<0)表示从右到左反向提取元素,即从start_index索引对应的元素开始反向每step个元素取出来一个，直到取到end_index+1对应的元素结束.
#此时start_index对应的元素要晚于end_index对应的元素出现,否则返回[]
##############################################################################################


#############
#######加法
#两种相同的序列才可以进行加法操作
l1=[1,2,4]
l2=[3,4,5]
l3=['8','9','10']
print('l1+l3=',l1+l3)
#print('l1+"abcdefg"=',l1+'abcdefg')
###注意此处l1和"abcdefg"不是相同的序列，无法进行加法操作
#########################################################################
#############################
############乘法
print('python*2=','python'*2)
print('l1*2=',l2*2)
print('(\'a\',\'b\')*2=',('a','b')*2)
##############################################################
#所有序列都可以进行如下操作：
#索引
#切片
#加
#乘
#检查某个元素是否属于序列成员（成员资格）
##############################################################
##成员资格指某值是否在序列中，
#使用in运算符，运算符结果为布尔值True 或者 False，语法如下：
number=[1,2,3,4,5,6,7,8,9,10]
str='abcdefg'
if 'ab' in str :
	print('yse, True')
else:
	print('No, False')
if 'ac' in str or 1 in number:
	print('Yes,True')
else:
	print('No, False')

if 'ac' in str :
	print('Yes,True')
else:
	print('No, False')
###事实证明字符串'ac'不是字符串str的部分
if 11 in number:
	print('True')
else:
	print('No, False')


#######################################
#
#序列长度、最小值和最大值,分别对应三个内置函数：
#len()
#min()
#max()
################################################
months=[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'Octber',
    'November',
    'December',]
length_1=len(months)
length_2=len('months')
print(length_1)
print(length_1)
#####注意比较两次输出的值分别为12和6
min=min(months)
max=max(months)
print(max)
print(min)
##用于找出manths列表中最长的和最短的元素，
#####################################












