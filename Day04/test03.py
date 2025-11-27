num1 = int(input(f'输入第一个整数:'))
max = num1
num2 = int(input(f'输入第二个整数:'))
if num2 > max:
    max = num2
num3 = int(input(f'输入第三个整数:'))
if num3 > max:
    max = num3
print(f'最大数为:{max}')
