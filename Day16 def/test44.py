# 递归调用辗转相除法
def gcd(n1, n2):
    global count
    count += 1
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


# 简化写法
# def gcd(n1, n2):
#     return n1 if n2 == 0 else gcd(n2, n1 % n2)
# 再简化写法
# gcd = lambda n1, n2: n1 if n2 == 0 else gcd(n2, n1 % n2)

# 定义一个count 计算这个算法实现用的次数
count = 0
a, b = eval(input(f'请输入两个整型数值, 并用逗号分隔: '))
print(gcd(a, b))
print(count)
