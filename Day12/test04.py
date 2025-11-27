color1 = ['red', 'blue', 'green', 'white', 'black', 'yellow', 'pink']
color2 = ['gray', 'orange', 'cyan', 'red', 'purple', 'blue', 'brown', 'blue']

# 删除 color2 中与 color1 相同的颜色
for color in color2:
    # 判断
    if color in color1:
        # 删除该颜色
        color2.remove(color)
        print(f'删除了{color}')
print(color2)
