# 列表为空, 在内存中有空间, 但没有元素
# 空列表不是None, None在Python中也是一个对象, 类型为Nonetype
x = []
# x在内存中有地址(空间)
print(id(x))

if x is None:
    print(f'x为None')
else:
    print(f'x不为None')