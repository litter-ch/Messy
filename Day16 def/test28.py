# locals(): 字典方式列出所有的局部变量名称与内容
# globals(): 字典方式列出所有的全局变量名称与内容

def func():
    language = 'Java'
    print(f'{locals()=}')


msg = 'Python'
print(f'{globals()=}')
func()
