def insert_number(number, my_list=None):
    # 判断, 如果列表为空, 则在调用函数时创建一个空列表
    if my_list is None:
        my_list = []
    my_list.append(number)
    print(my_list)


# 创建一个函数
number_list = [666, 888]

# 调用函数
insert_number(1, number_list)
insert_number(2, number_list)
# 多次调用
insert_number(2)
insert_number(3)

# 函数内部创建的列表, 函数弹栈以后地址就消失了
# 在外部创建列表, 地址不会消失
