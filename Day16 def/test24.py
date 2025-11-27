#  定义一个灵活的线性函数
def outer(k, b):
    def inner(x):
        return k * x + b
    return inner


# 调用函数
f1 = outer(1, 2)  # f1 = x + 5
print(f1(5))      # 5 + 5
print(f1(10))     # 10 + 5

# 在这里程序可以重复使用, 如果没有闭包(closure), 我们需要传递 k, b, x 三个参数
# 闭包(closure) 可以让程序设计更有效率, 同时未来扩充时程序更容易移植
f2 = outer(3, 4)  # f2 = 3x + 4
print(f2(5))      # 3 * 5 + 4
print(f2(10))     # 3 * 10 + 4
