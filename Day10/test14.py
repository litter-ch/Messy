# 列表嵌套列表
score = [['张三', '研究生1班', '2000/1/1'], 94, 87, 73]

name = score[0][0]
class_ = score[0][1]
birthday_ = score[0][2]
print(f'{name=}, {class_=}, {birthday_=}')

chinese = score[1]
math = score[2]
english = score[3]
print(f'{chinese=}, {math=}, {english=}')

# append拼接
# 格式: 对象.append(元素)
python = ['python', 100]
score.append(python)
print(score)