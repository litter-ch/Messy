def build_dict(name, age, **kwargs):
    '''
    建立学生成绩字典数据
    name : 学生姓名
    age : 学生年龄
    kwargs : 学生各科成绩数据
    '''
    score = {}
    score['name'] = name
    score['age'] = age
    print(f'{kwargs}, {type(kwargs)=}')
    # 遍历 kwargs 字典类型的数据
    for key, value in kwargs.items():
        score[key] = value
    # 循环结束后, 将 score 字典返回
    return score


# 函数名 : 地址
# 函数名()  : 函数调用
# 查看文档字符串 (Document string)
# 格式: help(函数名)
help(build_dict)

# 查看函数的注释
# 格式: 函数名.__doc__
print(build_dict.__doc__)
