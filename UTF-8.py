#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print (u'中文输出正常')
print('Hello %s, my name is %s' %('Jane' ,'Alex'))

L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][2])

#list and  tuple

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s!' %(name))
    #为什么不能写成 print('Hello,%s!', %(name))

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




while(1):
	print('bad boy')