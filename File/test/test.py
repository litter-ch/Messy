# 打开要复制的文件, 只读模式
# 打开副本文件, append模式

source_file = open('d.txt', 'r')
dst_file = open('d_bat.txt', 'a')

# 从源文件中读取内容
# 将读取的内容写入副本

while True:
    content = source_file.read(1024)
    if len(content) == 0:
        dst_file.write('\n')
        break
    print('-' * 20)
    dst_file.write(content)

# 关闭源文件和副本
source_file.close()
dst_file.close()
