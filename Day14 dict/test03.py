fruits = {'西瓜': 15, '香蕉': 20, '水蜜桃': 25, '梨': 20, '火龙果': 30, '无花果': 20}
print(fruits)

# 删除元素
del fruits['西瓜']
print(fruits)

# 使用pop() 方法删除
fruits.pop('无花果')
print(fruits)

# 如果删除的键值对不存在, 'NOT EXIST'
result = fruits.pop('人参果', 'NOT EXIST')
print(fruits, result)

# 随机删除 格式:字典.popitem()
fruits.popitem()
print(fruits)

# 清空字典, 字典本身还存在 为{}
fruits.clear()
print(fruits)

# 删除整个字典
del fruits  # 再输出这个字典程序会报错 NameError: name 'fruits' is not defined
