# 删除列表中所有的元素
fruits = ['apple', 'banana', 'cherry', 'watermelon', 'pear', 'strawberry', 'orange']
print(fruits)

# 注意 : 遍历与操作不能在同一个列表对象上进行
# 列表的切片复制
for fruit in fruits[:]:
    fruits.remove(fruit)
print(fruits)

