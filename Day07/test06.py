# 如果在字符串前添加r,其字符串内容的转义效果就消失了 (raw string) 原生字符串
# 使用场景: 文件路径, 网络资源地址中经常使用
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
s4 = s1 + '\n' + s2
print(s3)
print(s4)
print('good\ngirl')
print(r'good\ngirl')
