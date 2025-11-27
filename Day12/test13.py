# 哨兵值 用于控制 while循环的条件
# 定义一个哨兵值
active = True
while active:
    dialog = input()
    if dialog.lower() != 'q':
        print(dialog)
    else:
        # 修改哨兵值
        active = False
