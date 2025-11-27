a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# 交集 (intersection  &)
# 格式:集合1.intersection(集合2)  或  集合1 & 集合2
result1 = a.intersection(b)  # result1 = a & b
print(f'交集{result1=}')

# 并集 (union  |)
# 格式:集合1.union(集合2)  或  集合1 | 集合2
result2 = a.union(b)  # result1 = a | b
print(f'并集{result2=}')

# 差集 (difference  -)
# 格式:集合1.difference(集合2)  或  集合1 - 集合2
result3 = a.difference(b)  # result1 = a - b
print(f'a与b的差集{result3=}')

result4 = b - a
print(f'b与a的差集{result4=}')

# 对称差集(并集 - 交集) (symmetric_difference  ^)
# 格式:集合1.symmetric_difference(集合2)  或  集合1 ^ 集合2
result5 = a.symmetric_difference(b)  # result1 = a ^ b
print(f'对称差集{result5=}')

