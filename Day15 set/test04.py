a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = {3, 4, 5, 6, 7}
d = {1, 2, 3}

# isdisjoint()   判断两个集合是否没有交集
result1 = a.isdisjoint(b)
print(f'{result1=}')

result2 = a.isdisjoint(c)
print(f'{result2=}')

# issubset()   判断是否是另一个的子集
result3 = a.issubset(b)  # a 是 b 的子集?
print(f'{result3=}')

result4 = d.issubset(a)  # d 是 a 的子集？
print(f'{result4=}')

# issuperset()   判断是否是另一个的父集
result5 = a.issuperset(d)   # a 是 d 的父集？
print(f'{result5=}')

