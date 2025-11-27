names = ['张三', '李四', '王五', '刘七', '张三', '杨七']
# 从开始查找的位置查找元素第一次出现的索引(下标)
# 格式:对象.index(元素,开始找的位置)  不指定开始找的位置则默认第一个开始
name_index = names.index('张三')
print(f'{name_index=}')
name_index = names.index('张三', 1)
print(f'{name_index=}')

# 如果没找到元素,程序会报错  先用in判断
if '张三' in names[5:]:
    name_index = names.index('张三', name_index + 1)
    print(f'{name_index=}')
else:
    print(f'没找到')

# 获取指定元素在列表中出现的次数
name_count = names.count('张三')
print(f'{name_count=}')