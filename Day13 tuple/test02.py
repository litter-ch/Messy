# 修改元组中的元素
fruits = ("apple", "banana", "cherry")
print(fruits)

# fruits[0] = 'orange'
# print(fruits)   元组不能修改, 这样会报错
# TypeError: 'tuple' object does not support item assignment

# 修改的方式, 重新进行赋值, 覆盖掉原来的元组
fruits = ('orange', 'watermelon', 'peach')
print(fruits)

