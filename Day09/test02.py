# 简单面向对象概念
# 删除字符串空格
str = '   zhangsan  '
print(f'/{str}/')
str1 = str.lstrip()  # 格式:对象.lstrip()   l表示left 删除左边多余的空格
str2 = str.rstrip()  # 格式:对象.rstrip()   r表示right 删除右边多余的空格
str3 = str.strip()   # 格式:对象.strip()    两边都删除
print(f'/{str1}/ /{str2}/ /{str3}/')

# 提示用户输入用户名
account = input('请输入您的账号:')
print(account)
# 删除调用用户输入的左右两边空格
account = account.strip()
print(f'{account=}')

