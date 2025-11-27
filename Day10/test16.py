# 二维列表的相关操作
scores = [['张三', 99, 88, 77],
          ['李四', 88, 77, 66],
          ['王五', 88, 55, 99]]
scores[0][1] = 100
print(scores)

print(f'李四的全部信息:{scores[1]}')

print(f'王五的成绩:{scores[2][1:]}')