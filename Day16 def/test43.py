# 程序 = 算法 + 数据结构
# 辗转相除法
def gcd(n1, n2):
    global count
    # 找到较大数(默认: n1 > n2)
    if n1 < n2:
        # 交换位置
        n1, n2 = n2, n1
    # 循环判断
    while n2 != 0:
        # tmp 是余数
        tmp = n1 % n2
        # 交换
        n1, n2 = n2, tmp
        count += 1
    return abs(n1)


# 定义一个count 计算这个算法实现用的次数
count = 0

a, b = eval(input(f'请输入两个整型数值, 并用逗号分隔: '))
print(gcd(a, b))
print(count)

