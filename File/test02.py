# read(n), n: 从文件中读取的数据的长度, 没有指定 n 或小于 0 默认为所有内容
# readline(), 一次只读取一行内容, 读取完指针到下一行, 下次继续接着读取
# readlines(), 按行的方式读取所有内容, 返回的是列表, 每行内容就是列表的一个元素
# readable(), 判断是否可以读取, 可以返回True, 否则False
# write(), 返回写入的文件字节长度
# writeable(), 判断是否可以写入, 可以返回True, 否则False
# flush(), 立即清空缓冲区的数据内容到文件里面
# 一般情况 写的数据内容先在缓冲区, 缓冲满了,文件关闭或程序结束才会将内容写入文件

# 打开文件
f = open('b.txt')
f1 = open(r'C:\Users\鸡蛋\Desktop\test.txt')

# 读写文件
print(f1)
print(f1.read(2))
print(f1.name)

print(f.readline())
print(f.readline())

print(f.readable())

# 关闭文件
f.close()
f1.close()












