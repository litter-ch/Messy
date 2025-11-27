fruits = ['orange', 'watermelon', 'peach', 'apple', 'banana']
print(fruits[1:3])
print(fruits[:3])
print(fruits[::-1])

# 元组中的元素个数
print(len(fruits))

# 能够修改掉元素的方法在元组不能使用 append(), insert(), pop(), remove()...

# 元组与列表的类型互换
fruits_list = list(fruits)
print(fruits_list, type(fruits_list))

fruits_list.append('apple')
print(fruits_list, type(fruits_list))

fruits_tuple = tuple(fruits_list)
print(fruits_tuple, type(fruits_tuple))
