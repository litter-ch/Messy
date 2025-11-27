nations = [['中国', '北京'], ['美国', '华盛顿'], ['俄罗斯', '莫斯科']]
print(nations[0][1])

# 将双值序列列表转换为字典
nation_dict = dict(nations)
print(nation_dict)
print(nation_dict['中国'])

# 使用zip() 函数实现字典的快速建立
# 十六进制 : abcdef  10, 11, 12, 13, 14, 15
hex_digit = dict(zip('abcdef', range(10, 16)))
print(hex_digit)

# 1: 张三  2: 李四  3: 王五  4:刘六
names = ['张三', '李四', '王五', '刘六']
names_dict = dict(zip(range(1, 5), names))
print(names_dict)