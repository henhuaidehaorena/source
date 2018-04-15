#字典类似于通过联系人查找地址和联系人详细情况的通讯录
#即，键和值组成了key-value pair,注意，键必须是唯一的，
#如果恰巧有两个人重名的话，则无法找到正确的信息

##############
##只能使用不便的对象如字符串来作为字典的键，但是字典的值却是可以变化的
#一个典型的字典定义格式如下：
#dict={key_1:value_1,key_2:value_2}
##键和值之间通过冒号分割，键-值对之间通过逗号分割，
#键值对包含在花括号中
##############################
dict_test={'Michael':95,'Bob':75,'Tracy':85}
print('Michael\'s grade is',dict_test['Michael'])
##把数据放入dict的方法，除了初始化时指定以外，还可以通过key放入：
dict_test['Michael']=100
print('Michael\'s new grade is',dict_test['Michael'])
print(u'dict.get()函数的首次使用:',dict_test.get('Tracy'))
######如果key值不存在，则dict就会报错
#print('alex grade is',dict_test['Alex'])
#Traceback (most recent call last):
 # File "<stdin>", line 18, in <module>
#KeyError: 'Alex'
#若要避免key不存在导致的错误，可以通过in语句判断是否存在：
if 'Alex' in dict_test:
	print('that is true')
else:
	print('no, you are wrong\n')
#若要删除一个key,可以用过pop()实现
dict_test.pop('Bob')
print('new dict_test is',dict_test)
###########字典中键-值遍历方法
for key,value in dict_test.items():
	print(key,'=>',value)
print('\n')
#########方法二
for key in dict_test:
	print(key,'=>',dict_test[key])
#########推荐使用方法二，便于理解

####使用dict实现switch功能
#
#coding=gbk  
###################################################  
x = int(input("Enter the 1st number: "))  
y = int(input("Enter the 2nd number: "))  
  
def operator(o):  
    dict_oper = {  
        '+': lambda x, y: x + y,  
        '-': lambda x, y: x - y,  
        '*': lambda x, y: x * y,  
        '/': lambda x, y: x / y}  
    return dict_oper.get(o)(x, y)  
   
    o = raw_input("Enter operation here(+ - * /): ")  
print (operator('+'))
print (operator('-'))
print (operator('*'))
print (operator('/'))
##################################################################
##Python字典get()函数返回指定键的值，
#如果值不在字典中返回默认值。
#key -- 字典中要查找的键。
#default -- 如果指定键的值不存在时，返回该默认值值。


#################################################################################################
###set 集合
#set和dict类似，也是y一组key的集合，但是其不存储value,由于key不能重复，
#因此在集合中没有重复的key;
#创建一个集合:jiheming={a,b,c}
#增加一个key到集合中：jiheming.add(key)
#删除一个key:jiheming.remove(key)
########################################
#set可以看成数学意义上的无序和无重复元素的集合，
#因此，两个set可以做数学意义上的交集、并集,补集等操作：
s1={1,2,3}
s2={2,3,4}
print(s1&s2)
print(s1|s2)
print(s1-s2)#s1-s2指的是s1与s2的补集，即属于s1但不属于s2的key






