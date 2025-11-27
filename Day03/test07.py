"""
    逻辑运算符
"""
# and 一假为假
sex = int(input(f'输入性别（1为男，0为女）:'))
age = int(input(f'输入年龄:'))
result1 = sex == 1 and age >= 18
print(f'合格')
# or 一真为真
sex = int(input(f'输入性别（1为男，0为女）:'))
age = int(input(f'输入年龄:'))
result2 = sex == 1 or age >= 18
print(f'合格')
# not 将结果取反
# 使用场景 : if not 条件

num1 = 10
num2 = 20

result3 = num1 == num2
print(f'result3 = {not result3}')
print(f'result3 = {result3}')
# debug 可以查看程序的运行流程