score = [['001', '张三', 88, 76, 81, 0, 0, 0],
         ['002', '李四', 86, 72, 79, 0, 0, 0],
         ['003', '王五', 90, 76, 73, 0, 0, 0],
         ['004', '刘六', 82, 70, 67, 0, 0, 0],
         ['005', '杨七', 84, 65, 96, 0, 0, 0]]   # 第一个0:总分 第二个0:平均分 第三个0:排名

# 计算总分与平均分
for i in range(len(score)):
    # 总分
    score[i][5] = sum(score[i][2:5])
    # 平均分
    score[i][6] = round(score[i][5] / 3, 2)

# 总分排序 从高到低
score.sort(key=lambda x: x[5], reverse=True)

# 名次
ranking = 0   # 排序变量
for i in range(len(score)):
    ranking += 1
    # 判断
    if i >= 1:
        if score[i][6] == score[i-1][6]:   # 如果总分一样
            ranking -= 1    # 排序变量-1
    score[i][7] = ranking
    print(score[i])

# 以学号顺序查看
print('-'*20)
score.sort(key=lambda x: x[0])
for i in range(len(score)):
    print(score[i])
