# 定义一个函数, 修改文章内容
def modify_str(str):
    str = str.lower()
    # 处理标点符号
    for char in str:
        if char in '?,.':
            str = str.replace(char, '')
    return str


# 定义一个函数, 统计单词出现的次数
def count_words(str):
    str_list = str.split()  # split() 方法默认使用空格切割
    my_dict = {word: str_list.count(word) for word in str_list}
    return my_dict


composition = '''When I was small, my mother told me that apple was good 
for my health, because it contained so many vitamins. Since then, I almost 
eat an apple a day, I fall in love with apple. The apple not only tastes 
sweet, but also makes my skin look good,there is a saying that once an apple 
a day, keeps the doctor away. It really happens to me.'''

print(f'原始作文: ')
print(composition)

print(f'修改后的作文: ')
composition = modify_str(composition)
print(composition)

result = count_words(composition)
print(result)