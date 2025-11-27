# 捕获异常, 从上往下捕获, 捕获到了第一个就不向下继续捕获了
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except ValueError as v:  # 捕获异常, 出现这个异常执行这个语句
    print('只能输入数字', v)
except ZeroDivisionError as z:  # 捕获异常, 出现这个异常执行这个语句
    print('除数不允许为0', z)
else:  # 前面代码没有异常才会执行的代码
    print('通关')
    print(result)
finally:  # 不管有没有异常怎么都会执行的代码
    print('无敌')
print('程序结束')
