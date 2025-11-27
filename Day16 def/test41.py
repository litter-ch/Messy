# 最大公约数
def gcd(a, b):
    min_ = min(a, b)
    j = 1 if min_ < 0 else -1
    global count
    for i in range(min_, 2, j):
        count += 1
        if a % i == 0 and b % i == 0:
            return abs(i)
    else:
        return '没有'


# 定义一个count 计算这个算法实现用的次数
count = 0

a, b = eval(input(f'请输入两个整型数值, 并用逗号分隔: '))
print(gcd(a, b))
print(count)
