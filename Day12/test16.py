#  删除列表中所有指定元素
colors = ['red', 'green', 'black', 'blue', 'black', 'yellow', 'cyan', 'white', 'black']
color = 'black'
# while 循环与列表结合使用
while color in colors:
    # 操作
    colors.remove(color)

print(colors)

