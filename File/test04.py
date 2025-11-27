# os.name('旧文件名','新文件名')
# os.name('旧路径/旧文件名','新路径/新文件名')  新路径不存在会自动生成

import os

try:
    os.rename('cc.txt', 'c.txt')
    print('成功更改')

except FileNotFoundError:
    print('原文件名已经更改或文件名错误')


try:
    os.renames('Two/two.txt', 'One/one.txt')
    print('成功修改')
except FileNotFoundError:
    print('原文件路径已经修改或路径错误')


