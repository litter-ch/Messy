'''
#   三目运算符 ：if...else...双分支结构的缩写形式
    格式：
       结果1 if 条件 else 结果2
       结果1 ：条件成立时返回的结果
       结果2 ：条件不成立时返回的结果
'''
num1 = int(input(f'输入第一个整数:'))
num2 = int(input(f'输入第二个整数:'))
num3 = int(input(f'输入第三个整数:'))
second_max = num1 if num1 > num2 else num2
max = second_max if second_max > num3 else num3
print(f'max ={max}')