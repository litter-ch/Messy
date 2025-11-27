# 一般类型参数传递(整型, 浮点型, 字符串类型)  值传递
# 容器类型参数传递(列表, 字典, 元组, 集合)   地址传递


def greeting(names):
    '''打招呼函数 : names 表示列表数据类型的字符串数据'''
    for name in names:
        print(f"hello {name}")
        print(666)


# 定义一个列表
names = ['张三', '李四', '王五', '刘六']
greeting(names)
