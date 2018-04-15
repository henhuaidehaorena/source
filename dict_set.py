#Python内置了字典：dict的支持，dict全称dictionary，
#在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，
#需要两个list：
names=['Michael','Bob','Tracy']
scores=[95,75,85]
#给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，
#再从scores取出对应的成绩，list越长，耗时越长。

#如果用dict实现，只需要一个“名字”-“成绩”的对照表，
#直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
#用Python写一个dict如下,注意此处为花括号；
d={'Michael':95,'Bob':75,'Alexander':85}
#注意此处为中括号
print('d的值为：%s' %d)
val=d['Michael']
print(d['Michael'])
d['Michael']=100

#########################################
#删除一个key，可以使用pop(key)的方法
d.pop('Bob')
##############################################
#######
#set和dict类似，也是一组key的集合，但不存储value。
#由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
print('现在的d包含以下值',d)


#为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
#假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，
#直到找到我们想要的字为止，
#这种方法就是在list中查找元素的方法，list越大，查找越慢。
#第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，
#然后直接翻到该页，找到这个字。
#无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
#由于一个key只能对应一个value，
#所以，多次对一个key放入value，后面的值会把前面的值冲掉：
#如果key不存在，dict就会报错：
#>>> d['Jack'] = 90
#>>> d['Jack']
#90
#>>> d['Jack'] = 88
#>>> d['Jack']
#88
#>>> d['Thomas']
#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
#KeyError: 'Thomas'

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Jack' in d
d.get('Thomas')

#Python 字典(Dictionary) get()方法
#描述
#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

####################################################################
#语法
#get()方法语法：
#dict.get(key, default=None)
#注意：返回None的时候Python的交互环境不显示结果。

#参数
#key -- 字典中要查找的键。
#default -- 如果指定键的值不存在时，返回该默认值值。
#在实际编程中"default="是无需体现出来的，只要写出返回值即可
dict={'name': 'Zara','Age':27}
print('value:%s' %(dict['name']))
print('sex:%s' %dict.get('sex','No such data'))
##################################################################
