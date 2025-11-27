# 简单面向对象概念
str = 'abc'
# 格式:对象.isupper()   isupper判断是否全部大写
r1 = str.isupper()
print(f'{r1=}')

# 格式:对象.islower()   islower判断是否全部小写
r2 = str.islower()
print(f'{r2=}')

n = '123'
# 格式:对象.isdigit()   isdigit判断是否全部数字
r3 = n.isdigit()
print(f'{r3=}')

str0 = 'hello world'
# isalpha判断是否全部为字母 如果字符串有空格不满足条件
# 格式:对象.isalpha()
r4 = str0.isalpha()
print(f'{r4=}')