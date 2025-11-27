# 数据类型转换
"""
=>整型 int(变量)
=>浮点型 float(变量)
=>字符串型 str(变量)
"""
num1 = '10'
num2 = '20'
result = num1 + num2
print(f'num1为{type(num1)}')
print(f'result = {result}')
# result = 1020
# 网页中的输入框获取的数据，都是字符串类型
result = int(num1)+int(num2)
print(f'result = {result}')
# result = 30
n1 = int(num1)
n2 = int(num2)
result = str(n1 + n2)
print(result)
result = str(n1) + str(n2)
print(result)
"""
当字符串内容为浮点型要转换为整型时，无法直接用 int() 转换：
a='2.1'  # 这是一个字符串
print(int(a)) # 会报错 "invalid literal for int() "。
需要把字符串先转化成 float 型再转换成 int 型：
"""
a = '2.1'  # 这是一个字符串
print(f'a转化为整数为{int(float(a))}')

