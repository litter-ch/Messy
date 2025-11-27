def kitchen(unserved, served):
    ''' 将所有未服务的餐品转换为已服务的餐品 '''
    print('厨房正在备餐...')
    # 循环遍历 unserved 未服务的餐品列表
    while unserved:
        # 取出一个餐品
        current_meal = unserved.pop()
        # 模拟出餐的过程
        print(f'正在制作: {current_meal}')
        # 将制作完毕的餐品转入到已服务的餐品列表中
        served.append(current_meal)


def show_order_meal(unserved):
    ''' 显示客户点的所有餐品 '''
    print(f'下列是客户所有的餐品: ')
    # 判断
    if not unserved:
        print('**** 没有任何未服务的餐品 ****')
    for meal in unserved:
        print(meal, end=' ')
    print()


def show_served_meal(served):
    ''' 显示所有已经服务的餐品 '''
    print('下列是所有已经服务的餐品: ')
    # 判断
    if not served:
        print('**** 没有任何餐品 ****')
    for meal in served:
        print(meal, end=' ')
    print()


# 所点餐品
order_meal_list = ['剁椒鱼头', '青椒肉丝', '糖醋排骨']

# 定义一个制作完毕的餐品列表
served_list = []

# 查看制作前的所有餐品
show_order_meal(order_meal_list)

# 查看所有的服务餐品
show_served_meal(served_list)

# 将餐品传递给厨房, 实现餐品的制作
# 在传递 order_list 列表时, 应该传递该列表的复制品 (列表切片复制)
kitchen(order_meal_list[:], served_list)

print('-' * 50)

# 制作完毕后, 再次查看所有服务与未服务的餐品列表
show_order_meal(order_meal_list)
show_served_meal(served_list)
