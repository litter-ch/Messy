# 定义元组
numbers = (1, 2, 3, 4, 5)
print(numbers, type(numbers))

# 如果元组中只有一个元素, 该元素一定要添加逗号, 不能省略
color = ('red',)
print(color, type(color))

# 简便建立元组的方法
names = '张三', '李四', '王五', '刘六'
print(names, type(names))

# 读取元组中的元素
name1 = names[0]
name2 = names[1]
print(name1, name2)

# 简便的读取元组中的元素
n1, n2, n3, n4 = names
print(n1, n2, n3, n4)

# 遍历元组中的所有元素
for name in names:
    print(name)