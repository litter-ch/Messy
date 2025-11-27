# 自定义函数不会对主函数的变量进行修改, 只是在自定义函数内部定义了与主函数重名的变量
# 在主函数访问同名变量优先访问主函数的变量
# 在自定义函数内部访问同名变量优先访问自定义函数的变量
# 在自定义函数中如果要修改全局变量, 定义 global 关键字

def func():
    msg1 = 'Java'
    global msg2
    msg2 = 'english'


# 调用函数前
msg1 = 'Python'
msg2 = 'chinese'
print(f'{msg1=}, {msg2=}')

func()
# 调用函数后
print(f'{msg1=}, {msg2=}')
