# 闭包可以访问外部函数的变量, 但不能进行修改
# 如果要访问并修改外部函数的变量, 定义 nonlocal 关键字
# nonlocal 访问且可以修改上一层函数(有要访问的变量)的变量
def outer():
    z = 666

    def inner():
        global x
        # nonlocal 表示访问上一层函数(有变量z)的变量 z
        nonlocal z
        z = 100
        print(f'inner 输出: {x=}')
        print(f'inner 输出: {z=}')

    # 外层函数直接调用内层函数
    inner()


x = 1
y = 2
print(f'主函数: {x=}')
print(f'主函数: {y=}')

# 在主函数中直接调用外层函数
outer()
