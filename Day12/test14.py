# 外层循环(行)
i = 1
while i <= 9:
    # 内层循环(列)
    j = 1
    while j <= i:
        print(f'{j}*{i}={j*i}', end=' ')
        # 内层循环的控制变量
        j = j + 1
    # 外层循环的控制变量
    i = i + 1
    # 换行
    print()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j, i}', end=' ')
#     print()