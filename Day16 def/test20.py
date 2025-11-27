def multiply(*args):
    wul = 1
    for i in args:
        wul *= i
    return wul


def run_multiply_args(func, *args):
    return func(*args)


# 调用函数
result = run_multiply_args(multiply, 1, 2, 3, 4, 5)
print(result)


