# 字典的定义格式: {key1: value1, key2: value2, key3: value3, ... , keyN: valueN}
fruits = {'西瓜': 15, '香蕉': 20, '水蜜桃': 25}
print(fruits, type(fruits))

# 从字典中取值 : value = 字典名称[key]
price = fruits['水蜜桃']
print(price)

# 添加元素到字典中 : 字典名称[key] = value
# 如果字典中 key 已经存在, 数据会覆盖.(key是不能重复的)
fruits['橘子'] = 18
fruits['西瓜'] = 12
print(fruits)
