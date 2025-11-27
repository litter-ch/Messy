# 装饰器 : 参数, 接受一个函数    返回值, 返回另一个新函数
def upper(func):
    # 定义一个新函数
    # 参数说明 : *args 接受任意个数的一般参数   **kwargs 接受任意个数的关键字参数
    def new_func(*args, **kwargs):
        print(f'函数名称: {func.__name__}')
        print(f'函数参数: {args = }, {kwargs = }')
        # 执行旧函数
        result = func(*args)
        # 处理之前函数返回的结果
        new_result = result.upper()
        return new_result

    return new_func


# 打招呼函数
@upper  # 自动设置装饰器(为该函数增添了一个新功能)
def greeting(*names):
    names_str = ''
    for name in names:
        names_str += name + ' '
    return 'Hello ' + names_str


print(greeting('张三', '李四'))
