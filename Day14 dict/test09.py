# 建立一个士兵列表
armys = []

colors = ['red', 'blue', 'green']
scores = [3, 5, 7]
speeds = ['slow', 'medium', 'fast']

# 建立 50 个士兵
for soldier_num in range(50):
    if soldier_num % 3 == 0:
        soldier = {'tag': colors[0], 'score': scores[0], 'speed': speeds[0]}
    elif soldier_num % 3 == 1:
        soldier = {'tag': colors[1], 'score': scores[1], 'speed': speeds[1]}
    else:
        soldier = {'tag': colors[2], 'score': scores[2], 'speed': speeds[2]}
    # 将创建的士兵添加到 armys 列表中
    armys.append(soldier)

for soldier in armys[10:21]:
    print(soldier)