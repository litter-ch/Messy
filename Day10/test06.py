numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 删除列表中的元素   del
del numbers1[0]
print(numbers1)

# 切片删除
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers2[:3]
print(numbers2)
print(numbers2[:5])

# 使用step控制删除的步长
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers3[::2]
print(numbers3)
print(numbers3[::2])

# 删除整个列表 后续代码将无法继续使用列表变量
del numbers3
print(numbers3)


