# 建立市场调查的空字典
survey_dict = {}

# 哨兵值(初始值一般为 True)
market_survey = True
while market_survey:
    name = input(f'请输入您的名字: ')
    spot = input(f'梦幻旅游景点: ')
    # 将信息存储在字典中
    survey_dict[name] = spot
    # 询问
    repeat = input('是否还有人需要进行市场调查(y/n): ')
    # 判断
    if repeat.lower() == 'n':
       market_survey = False

# 查看调查的数据
for name, spot in survey_dict.items():
    print(f'{name}的梦幻旅游景点为{spot}')