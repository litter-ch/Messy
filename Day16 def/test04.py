# 设计函数的默认参数
# 默认参数之后的所有参数都要有默认值
def interest(name, interest_type='旅游', subject='西藏'):
    '''显示兴趣和主题'''
    print(f'{name}的兴趣是: {interest_type}')
    print(f'在{interest_type}中,最喜欢的是: {subject}')


# 调用的形式
interest('张三', '旅游', '西藏')
interest('李四', '美食', '臭豆腐')
interest('王五', '游戏', '俄罗斯方块')
interest('默认')
# 关键字传参
interest(interest_type='拍照', subject='小姐姐', name='赵六')