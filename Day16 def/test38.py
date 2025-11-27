# 装饰器 : 参数, 接受一个函数    返回值, 返回另一个新函数
def errcheck(func):
    def new_func(*args):
        if args[1] != 0:
            # 如果除数不为 0,则执行原函数
            return func(*args)
        else:
            # 除数为 0, 不调用原函数
            return '除数不能为 0'
    return new_func


# 自定义一个除法函数
# 为这个除法函数增添一个新功能, 检查除数是否为 0
@errcheck
def my_division(x, y):
    v = x / y
    return v


print(my_division(5, 2))
print(my_division(5, 0))
