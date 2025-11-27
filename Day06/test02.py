# Python提供了两种循环的实现方式，while循环和for循环

# 求1~100的累加和
# 已知循环次数的条件下使用  / for 循环实现   for + range
n = 0
for i in range(1, 101, 1):
    n += i
print(n)

# 不知道循环次数的情况下使用 / while 循环实现   while True + break
m = 0
x = 1
while x <= 100:
    m += x
    x += 1
print(m)
