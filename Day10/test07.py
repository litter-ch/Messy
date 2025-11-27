# 判断列表是否为空(是否存在元素)
# 自定义变量名称与Python内置函数名称相同, 在自定义变量之后添加_用于区分
numbers = [1, 2, 3, 4, 5]
print(numbers)
len_ = len(numbers)
if len_:
    print('这不是一个空列表')
else:
    print('这是一个空列表')

# *c 表示c变量可以接受多个数值 把剩下没有被接受的数值 返回成一个列表
a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)

x, *y, z = 1, 2, 3, 4, 5
print(x, y, z)


