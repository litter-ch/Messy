# 1=>石头 2=>剪刀 3=>布
import random
computer = random.randint(1,3)
root = int(input(f'请输入您的(1:石头,2:剪刀,3:布):'))
print(f'computer={computer}')
if computer == root:
    print(f'平局')
else:
    # 如果 if 语句中的条件过长，可以用接续符 \ 来换行。
    # \后的一行要缩进没有要求，可无序缩进，但我们保持代码的可读性一般设置同样的缩进格式。
    if computer == 1 and root == 2 \
         or computer == 2 and root == 3 \
         or computer == 3 and root == 1:
        print(f'computer赢')
    else:
        print(f'root赢')