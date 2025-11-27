# 嵌套函数
def distance(x1, y1, x2, y2):
    # 定义一个开根的内部函数
    def my_sqrt(z):
        return pow(z, 1/2)
    dx = pow((x1 - x2), 2)
    dy = pow((y1 - y2), 2)
    return my_sqrt(dx + dy)


# 调用函数
result = distance(3, 7, 6, 3)
print(f'{result=}')