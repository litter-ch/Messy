# 异常处理(捕获异常)
# try:
# 不确定是否能够正常执行的代码
# except:
# 如果检测异常, 就执行这个位置的代码
# else:
# 前面代码没有异常才会执行的代码
# finally:
# 不管有没有异常怎么都会执行的代码
# 可以声明捕获异常类型, 但是遇到其他异常类型时依然会报错, 无法捕获异常
s = [1, 2, 3]

try:
    print(abc)
except (NameError, TypeError):
    # 当要捕获多个异常类型时, 可以把要捕获的异常类型放元组里
    print('这一行代码有错误!')

try:
    print(s[3])
except BaseException as e:
    print('这一行代码有错误!')
    print(e)  # 输出异常信息
