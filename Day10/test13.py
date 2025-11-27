names = ['张三', '李四', '王五', '刘六']
#     连接列表中各个元素
#     使用 # 特殊字符连接, 连接后会返回一个新的字符串
#  格式:char.join(列表)
str1 = '#'.join(names)
print(f'{names=}\n{str1=}')

# 使用love 将列表中各个元素实现连接
str2 = 'love'.join(names)
print(f'{names=}\n{str2=}')

str3 = '123'.join(names)
print(f'{names=}\n{str3=}')