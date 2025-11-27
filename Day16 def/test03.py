# 多个参数
def interest(name, interest_type, subject):
    '''显示兴趣和主题'''
    print(f'{name}的兴趣是: {interest_type}')
    print(f'在{interest_type}中,最喜欢的是: {subject}')


# 调用的形式
interest('张三', '旅游', '西藏')
interest('李四', '美食', '臭豆腐')
interest('王五', '游戏', '俄罗斯方块')

# 关键字传参
interest(interest_type='拍照', subject='小姐姐', name='赵六')
