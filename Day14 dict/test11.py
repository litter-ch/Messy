# 字典内键的值是字典
Data = {'Jack': {'chinese_name': '杰克', 'city': '北京', 'age': 20},
          'James': {'chinese_name': '詹姆斯', 'city': '上海', 'age': 22},
          'Lucy': {'chinese_name': '露西', 'city': '深圳', 'age': 18},
          'Rose': {'chinese_name': '柔丝', 'city': '深圳', 'age': 19}}

# 元素的遍历
for name, information in Data.items():
    print(f'{name}的详细信息为: ')
    # information 是一个字典类型
    for key, value in information.items():
        print(f'{key=}: {value=}')
