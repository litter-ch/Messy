names = ['张三', '李四', '王五', '刘六']
print(f'{names=}')

# 将列表转换为enumerate对象, 可以设置enumerate对象的开始索引值, 如果不设置默认为0
# enumerate(序列, start = 索引值)
enumerate_names = enumerate(names, start=5)
print(f'{enumerate_names=}')

# 将 enumerate对象转换成 list类型
print(list(enumerate_names))


