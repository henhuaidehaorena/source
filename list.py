#列表list中的项目应该包括在中括号中
#一旦创建一个列表，就可以添加、删除、修改、排序或是搜索列表中的项目
#因此，列表是可变的数据类型
#this is my shopping list
shoplist=['apple','banana','pineapple','carrot','watermelon']
print(shoplist)
shoplist.append('egggggggg')
print(shoplist)
shoplist.remove('banana')
print(shoplist)
del shoplist[2]
print(shoplist)
shoplist.sort()
print(shoplist)
shoplist.reverse()
print(shoplist)

#########################################
#####修改
	
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
#此时motorcycles的值为['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print (motorcycles)
#此时motorcycles的值改为['ducati','yamaha','suzuki']

##############################################
###########增加元素
####在列表末尾添加元素：.append()
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles.append('lifan')
print (motorcycles)
motorcycles.append('ducati')
print (motorcycles)
##############在列表中插入元素：.insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles.insert(0, 'changan')
print (motorcycles)

#########根据索引删除：del，无法继续使用
motorcycles=['honda', 'yamaha', 'suzuki']
print (motorcycles)
del motorcycles[1]
####注意del的用法和.pop()函数不同,
#del删除后元素无法使用，pop删除末尾后可以继续使用
print (motorcycles)
#################################
#########.pop()删除末尾的元素，也可以根据索引删除，如motocycles.pop(0)
motocycles = ['honda', 'yamaha', 'suzuki']
print (motocycles)
motocycles.pop()
print(motocycles)
motocycles.pop(0)
print(motocycles)
###为什么同样是函数，pop()和del的引用方法不一样？
###############################################
#####.remove()不知道索引时，根据值删除元素
motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motocycles)
motocycles.remove('ducati')
print(motocycles)

############.sort() 永久性排序  反方向排序：sort(reverse = True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
##########################
###临时性排序：.sorted() 反方向排序：sorted(reverse = True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
linshi=sorted(cars)
#linshi=cars.sorted()
print(linshi)
print(cars)
#cars的值仍然为['bmw', 'audi', 'toyota', 'subaru']，没有发生变化

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
linshi=sorted(cars,reverse=True)
print('linshi',linshi)
print(cars)
########.reverse()永久性反转列表元素即第0位和最后一位互换数值，

cars = ['bmw', 'audi', 'toyota', 'subaru']
print ('It is a new file', cars)
cars.reverse()
print(cars)
#结果如下：
#It is a new type ['bmw', 'audi', 'toyota', 'subaru']
#['subaru', 'toyota', 'audi', 'bmw']

#len()函数使用方法
str = "runoob"
print(len(str))          # 字符串长度

l = [1,2,3,4,5]
print(len(l))               # 列表元素个数
















