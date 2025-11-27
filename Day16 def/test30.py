# 一般函数使用 def 关键字定义
def square(x):
    x = pow(x, 2)
    return x


# 匿名函数使用 lambda 定义
#  格式:  lambda参数列表: 执行语句
a = lambda x: pow(x, 2)
print(a(5))
