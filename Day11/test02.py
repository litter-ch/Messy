str = 'Python'

# 字符串中的元素无法更改
# 将字符串转换为列表再更改
str_list = list(str)
print(f'{str_list=}')

# 拼接
str_list.append('AI')
print(f'{str_list=}')

# 切片赋值
str_list[6:] = 'AI'
print(f'{str_list=}')