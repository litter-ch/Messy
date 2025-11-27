# 一般类型参数传递(整型, 浮点型, 字符串类型)  值传递
def change_number(n):
    ''' n 表示整型 '''
    n = 666


x = 100
# 调用函数
change_number(x)
print(x)