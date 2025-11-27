# 定义一个字典数据
names = {'Jack': 20, 'Peter': 22, 'Lucy': 18, 'Rose': 19, 'Lily': 18, 'Tom': 22, 'William': 19}

# 使用sorted 内置函数排序
names_keys = sorted(names.keys())
for key in names_keys:
    print(key, names[key])

names_values = sorted(names.values())
for value in names_values:
    print(value)