str = 'abcdefghiabcdopqxyz'

# 查找子串的方法
# .find()    从左开始找,如果找到,回传第一次出现的索引; 没有找到, 回传-1
# .rfind()   从右开始找,如果找到,回传最后出现的索引; 没有找到, 回传-1
# .index()   从左开始找,如果找到,回传第一次出现的索引; 没有找到, 程序报错
# .rindex()  从右开始找,如果找到,回传最后出现的索引; 没有找到, 程序报错

index = str.find('abc')
print(f'左边第一次出现的索引{index=}')
rindex = str.rfind('abc')
print(f'右边第一次出现的索引{rindex=}')
# 如果子串不存在，返回-1
idx = str.find('666')
print(f'{idx=}')

# 子串出现的次数    字符串.count(子字符串)
count_ = str.count('abc')
print(f'{count_=}')

# .isalnum() 返回True或False
# 判断原字符串是否仅有字母与数字
result = str.isalnum()
print(f'{result=}')