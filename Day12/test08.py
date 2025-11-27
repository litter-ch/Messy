colors = ['red', 'green', 'blue']
shapes = ['square', 'circle', 'diamond']

# 排列组合
result = [[color, shape] for color in colors for shape in shapes]
print(result)

# 打印输出列表元素的列表
# list unpacking 列表的拆解过程
for color, shape in result:
    print(f'{color=}, {shape=}')