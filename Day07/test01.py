# divmod()内置函数  获得商和余数 divmod(x,y)
q, r = divmod(10, 3)
print(q, r)

x, y = 10, 20
print(x, y)
# 交换x,y的值
# 方法一 定义一个临时变量实现数值交换
tem = x
x = y
y = tem
print(x, y)
# 方法二 赋值运算符的多重指定
x, y = y, x

a = 10
print(a)
# 删除不需要再次被使用的变量,其变量的空间内存将会被回收
del a






