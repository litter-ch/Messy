# 实现计算一次函数 : 5x + 10
def outer():
    # 外部函数的变量
    b = 10
    def inner(x):
        return 5 * x + b
    # 返回内部函数对象
    return inner


# 调用函数
func = outer()   # func 就是线性函数 f(x) = 5x + 10
print(func(1))
print(func(func(1)))