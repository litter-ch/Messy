# 定义一个士兵
soldier = {'tag': 'red', 'score': 3, 'x': 100, 'y': 100, 'speed': 'fast'}
print(f'士兵的坐标为:x = {soldier['x']}, y = {soldier['y']}')

# 判断
if soldier['speed'] == 'slow':
    x_move = 1
elif soldier['speed'] == 'medium':
    x_move = 3
else:
    x_move = 5

# 修改
soldier['x'] += x_move
print(f'士兵的坐标为:x = {soldier['x']}, y = {soldier['y']}')