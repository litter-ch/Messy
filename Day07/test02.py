# 年利率 计算本金和
money = 50_000
year = 1
while year <= 5:
    money += money * 0.015
    year = year + 1
print(f'本金和是:{money:.2f}')
# .2f 小数点保留两位

# 导入数学模块
import math

r = 5         # 定义圆的半径
# math.pi 取出数学模块中的pi
area = math.pi * r ** 2
print(area)

circumference = 2 * math.pi * r
print(circumference)

