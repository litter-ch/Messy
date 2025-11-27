# 字典生成器  字典 = {键表达式: 值表达式 for 表达式 in 可迭代对象}
# 将字符串中每个字母出现的次数列出来
# 字典 = {字母: 字母出现的次数 for 字母 in 字符串}
word = 'hello world'

alphabet_count = {alphabet: word.count(alphabet) for alphabet in word}
print(alphabet_count)

composition = '''when i was small my mother told me that apple was good 
for my health because it contained so many vitamins since then i almost 
eat an apple a day i fall in love with apple the apple not only tastes 
sweet but also makes my skin look good there is a saying that once an apple 
a day keeps the doctor away it really happens to me'''

# 实现字符串的切割
composition = composition.split()
print(composition)

word_dict = {word: composition.count(word) for word in composition}
print(word_dict)