# 容器类型参数传递(列表, 字典, 元组, 集合)  地址传递
def change_number(n):
    ''' n 表示列表数据类型 '''
    n[0] = 666


x = [100]
# 调用函数
change_number(x)
print(x)