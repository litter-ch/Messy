def insert_number(number, my_list=[666, 888]):
    my_list.append(number)
    print(my_list)


# 调用函数
insert_number(1)

# 多次调用
insert_number(2)
insert_number(3)

# 参数上定义列表, 地址不会消失
