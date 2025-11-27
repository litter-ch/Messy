# 程序 = 算法 + 数据结构
# 更相减损数
def lcm(a, b):
    x = abs(max(a, b))
    y = abs(min(a, b))
    global count
    count += 1
    if x % y == 0:
        return y
    else:
        return lcm(x - y, y)


# 定义一个count 计算这个算法实现用的次数
count = 0

a, b = eval(input(f'请输入两个整型数值, 并用逗号分隔: '))
print(lcm(a, b))
print(count)
