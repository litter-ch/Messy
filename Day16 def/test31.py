# 线性函数 2x + b
def func(b):
    def inner(x):
        return 2 * x + b

    return inner


f1 = func(3)
print(f'{f1(2)=}')


def func(b):
    return lambda x: 3 * x + b


f2 = func(4)
print(f'{f2(2)=}')
