a = 10
b = 10

# is 判断的是内存地址 注意:整型数值一样则内存地址也一样
r1 = a is b
print(f'{id(a)=}, {id(b)=},{r1=}')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
r2 = list1 is list2
print(f'{id(list1)=}, {id(list2)=},{r2=}')