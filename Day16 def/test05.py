def substract(x, y):
    '''减法设计'''
    r = x - y
    return r


def addition(x, y):
    '''加法设计'''
    return x + y


# 提示用户输入
a, b = eval(input('请输入两个整型数值, 并用逗号分隔: '))
operation = eval(input('请输入要执行的操作(1加法 2减法): '))
if operation == 1:
    # 如果调用的函数有返回值, 要接受返回值
    result = addition(a, b)
    print(f'{a}+{b}={result}')
elif operation == 2:
    result = substract(a, b)
    print(f'{a}-{b}={result}')
else:
    print('操作有误')