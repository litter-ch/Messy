# 函数的定义不会对程序造成任何的执行效果, 除非在程序编写处主动调用了该函数, 此时函数才会被执行
# 定义一个函数(打招呼函数)
def greeting():
    '''打招呼函数 : 第一个 Python 函数设计'''
    print("hello world")
    print(666)
    return  # 如果函数没有返回值, 在函数的末尾会自动添加 return 关键字, 此时默认返回为 None

# 调用函数,  格式 : 函数名()
# 小括号一定不能忘记书写, 如果仅有函数名, 此时函数名仅代表一个内存地址, 不会有任何执行效果
# 函数名仅仅代表的是该函数在内存中存储的空间地址, 不代表执行该函数
print(f'{greeting=}')
result = greeting()
print(f'{result=}')
greeting()
greeting()