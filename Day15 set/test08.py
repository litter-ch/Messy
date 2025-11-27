# 集合生成式
x = {i for i in range(1, 11)}
print(x)

y = {pow(i, 2) for i in range(1, 11)}
print(y)

z = {i for i in range(1, 101) if i % 3 == 0}
print(z)