money = 100
withdrawal_money = int(input(f'输入金额:'))
if money >= withdrawal_money:
    money -= withdrawal_money
    print(f'余额为:{money}元')
    print(f'取走{withdrawal_money}元')
else:
    print(f'余额不足')
choice = input(f'需要退卡吗(1退卡，0不退)')
if choice == '1':
    print(f'收好您的卡')
elif choice == '0':
    print(f'执行其他操作')
else:
    print(f'输入错误')

