# 文件名.tell  返回读取文件当前的指针位置
# 文件名.seek(偏移量, [0, 1, 2])  默认为0: 开头   1: 当前位置  2: 文件末尾
# 1 / 2 必须在二进制文件操作模式下(带b)
# 偏移量  改变读取文件指针位置偏移n

f = open('a.txt', 'rb')

print(f.tell())
f.seek(3)
print(f.tell())
f.seek(3, 1)
print(f.tell())
print(f.read())
print(f.tell())

f.close()
