import os
# os.getcwd() 获取当前目录路径
# os.listdir('目录')    获取目录里的文件名, 返回的是一个列表
# os.chdir('目标目录')  改变当前Python程序的工作目录, 让后续的文件操作基于目标目录进行
# ./ : 表示当前所在目录
# ../ : 表示上一级目录


print(os.getcwd())

print(os.listdir())

os.chdir('One')

print(os.listdir())