a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = {3, 4, 5, 6, 7}
d = {1, 2, 3}

# intersection_update() 更新集合1的元素为集合1 & 集合2 (集合1与集合2的交集)
print(f'{a=},{c=}')
a.intersection_update(c)  # 更新 a 的元素为 a 与 b 的交集
print(f'{a=},{c=}')

# update()  更新集合1的元素为集合1 | 集合2 (集合1与集合2的并集)
a.update(c)  # 更新 a 的元素为 a 与 b 的并集
print(f'{a=},{c=}')

# difference_update()  更新集合1的元素为集合1 - 集合2  (集合1与集合2的差集)
print(f'{a=},{b=}')
a.difference_update(b)
print(f'{a=},{b=}')

# symmetric_difference_update() 更新集合1的元素为集合1 ^ 集合2  (集合1与集合2的对称差集)
print(f'{a=},{b=}')
a.symmetric_difference_update(b)
print(f'{a=},{b=}')
