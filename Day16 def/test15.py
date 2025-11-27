# ** 表示关键词参数, 相当于'键值对'参数
# kwargs => keyword arguments 关键词形参
def build_dict(name, age, **kwargs):
    ''' 建立学生成绩字典数据 '''
    score = {}
    score['name'] = name
    score['age'] = age
    print(f'{kwargs}, {type(kwargs)=}')
    # 遍历 kwargs 字典类型的数据
    for key, value in kwargs.items():
        score[key] = value
    # 循环结束后, 将 score 字典返回
    return score


zhangsan_dict = build_dict('张三', 20, chinese=90, math=95, english=70, python=75)
print(zhangsan_dict)

score_dict = {'chinese': 89, 'math': 70, 'english': 90, 'python': 75}
list_dict = build_dict('李四', 18, **score_dict)
print(list_dict)
