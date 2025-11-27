files = ['1.txt', '2.jpg', '3.py', '4.txt', '5.jpg', '6.txt']
# 将所有的 txt 文件存储在一个列表中
# 定义一个空列表
txt = []

# 循环 files 列表
for file in files:
    if file.endswith('.txt'):
        txt.append(file)

# 循环结束后, 查看列表中的数据
print(f'{txt=}')
