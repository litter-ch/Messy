# 文件 存储在某种长期储存设备上的一段数据
# 打开文件
# 读写文件
# 关闭文件

# 文件名.name: 返回要打开的文件的文件名, 可以包含文件的具体路径(绝对路径)
# 文件名.mode: 返回文件的访问模式
# 文件名.closed: 检测文件是否关闭, 关闭返回True  反之False
f = open('a.txt')


print(f.name)

print(f.mode)

print(f.closed)

f.close()
print(f.closed)