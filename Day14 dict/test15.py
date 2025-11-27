composition = '''When I was small, my mother told me that apple was good 
for my health, because it contained so many vitamins. Since then, I almost 
eat an apple a day, I fall in love with apple. The apple not only tastes 
sweet, but also makes my skin look good,there is a saying that once an apple 
a day, keeps the doctor away. It really happens to me.'''

print(f'原始作文: {composition}')
print(' - ' * 40)

# 小写作文
composition = composition.lower()
print(f'小写作文: {composition}')
print(' - ' * 40)

# 标点符号改为空字符
for ch in composition:
    if ch in ".?,":
        # 替换
        composition = composition.replace(ch, '')
print(f'没有标点符号的作文:{composition}')
print(' - ' * 40)

# 实现字符串的切割
composition = composition.split()
print(composition)

# 定义一个空字典
word_dict = {}
# 统计列表中每一个元素出现的次数
for word in composition:
    # 判断
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)