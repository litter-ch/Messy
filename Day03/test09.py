# 定义变量，提示并接受用户的输出
score = int(input(f'请输入成绩:'))
# 判断
if score >= 60:
    print(f'奖励')
    print(f'玩')
else:
    print(f'惩罚')
    print(f'不玩')
print(f'程序继续执行...')

