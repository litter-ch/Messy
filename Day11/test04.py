str_list = ['P', 'y', 't', 'h', 'o', 'n']

# join() 将列表元素连接/结合返回一个字符串
#  格式:char.join(列表)
str = "".join(str_list)
print(str)

path = ['D:', '前端', '源码', 'picture', '1.jpeg']
absolute_path = '\\'.join(path)
print(absolute_path)
