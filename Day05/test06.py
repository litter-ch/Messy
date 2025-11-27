# 1.定义循环变量
i = 1

# 循环中计数的变量一定要在循环外部定义
count = 0

# 2.循环条件
while i <= 100:

     # 判断
    if i % 3 == 0:
        # 记录
        count += 1
    i += 1
print(count)