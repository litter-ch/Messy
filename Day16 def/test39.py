# 加粗标签装饰器
def bold(func):
    def wapper_func(x):
        print('b1')
        return '<b>' + func(x) + '</b>'
    print('b2')
    return wapper_func

# 大写装饰器
def upper(func):
    def new_func(args):
        print('u1')
        result = func(args)
        new_result = result.upper()
        return new_result
    print('u2')
    return new_func

@bold
@upper  # 装饰器依次往上执行
def greeting(str):
    return 'Hello ' + str

print(greeting('Python'))
