def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def running(func, arg1, arg2):
    # 调用传入的 func 函数, 并将参数传递给 func 函数
    return func(arg1, arg2)


# 函数可以作为参数实现传递
r1 = running(add, 10, 20)
print(f'{r1=}')

r2 = running(mul, 10, 20)
print(f'{r2=}')