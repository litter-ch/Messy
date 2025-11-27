a = [1, 2, 3, [4, 5, 6]]
# 浅复制 两个独立的空间对象,  里面包含的子空间对象是不独立的
# 格式:复制对象=被复制对象.copy()
b = a.copy()
print(f'id(a)={id(a)}\nid(b)={id(b)}')
print(f'{a=},{b=}')
print(f'{id(a[3])=},{id(b[3])=}')

# 外层元素不会联动
a.append(7)
print(f'{a=},{b=}')

# 浅复制会造成子元素的联动
a[3].append(8)
print(f'{a=},{b=}')

