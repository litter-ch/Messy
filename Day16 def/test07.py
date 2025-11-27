def simple_operation(x, y):
    '''简单的数学四则运算:
    x : 第一个整型数字
    y : 第二个整型数值
    return : 返回 x, y 运算的加减乘除'''
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    # 回传字典类型的数据
    data_dict = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    return data_dict


# 提示用户输入两个整型数值
a, b = eval(input('请输入两个整形数值, 并用逗号隔开: '))
# 调用函数
result = simple_operation(a, b)
print(f'{result=},{type(result)=}')