path = 'https://www.baidu.com/s?ie=UTF-8&wd=python'

# 是否以指定字符开头  格式:字符串.startswith(指定字符)
protocol = path.startswith('https://')

# 是否以指定字符结尾  格式:字符串.endswith(指定字符)
page = path.endswith('.html')
print(f'{protocol=}, {page=}')

# 字符内容替换(字符串本身是常量)  格式:字符串.replace(原字符,替换字符)
# 原字符串没有更改, 返回一个新的被更改的字符串
path1 = path.replace('python', '.html')
print(f'{path=}')
print(f'{path1=}')
