# 合并列表extend()

data = []

score1 = [['张三', '研究生1班', '2000/1/1'], 94, 87, 73]
# 扩展到空列表
# 格式: 对象.extend()
data.extend(score1)
print(data)

score2 = [['李四', '研究生2班', '2000/8/7'], 79, 66, 61]
data.extend(score2)
print(data)

# += 操作与 extend() 扩展实现的操作是相同的
score3 = [['王五', '研究生3班', '2000/6/4'], 88, 77, 66]
data += score3
print(data)

