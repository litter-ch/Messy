# 定义一个字典数据
names = {'Jack': 20, 'Peter': 22, 'Lucy': 18, 'Rose': 19, 'Lily': 18, 'Tom': 22, 'William': 19}

# 遍历字典
# items() 回传的是一个元组
for item in names.items():
    print(item)

for name, age in names.items():
    print(f'{name=}, {age=}')

# keys() 获取所有的 key键
for key in names.keys():
    print(key)

# value() 获取所有的 value值
for value in names.values():
    print(value)