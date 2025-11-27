# 循环体确定的循环
# 死循环 : while True:永远不会结束的循环
i = 1
while i <= 10:
    print(f'你好', i)
    i += 1
import random
import math
x = random.randint(1, 100)
y = random.randint(1, 100)
print(x, y)

i = min(x, y)
while i <= max(x, y):
    print(i, end='\t')
    i += 1
