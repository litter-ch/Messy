# os.remove('文件路径')  删除文件, 文件不存在会报错
# os.rmdir(空目录的路径) 删除目录, 文件夹非空会报错
# os.removedirs(空目录的路径)  递归删除目录, 往上依次删除,  文件夹非空会报错

import os

# os.mkdir(文件名) 创建文件

try:
    os.mkdir('a')
    print('创建成功')

except (FileExistsError, FileNotFoundError):
    print('不能创建多级目录或文件已经创建')

