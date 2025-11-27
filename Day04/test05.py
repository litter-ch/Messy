# 需求 : 会员/非会员   购买的价格
member = input(f'是否为会员(1:会员，0:非会员):')
money = int(input(f'消费的价格为:'))
if member == '1':
#     会员
    if money >= 200:
        print(f'打八折:')
    elif money >= 100:
        print(f'打九折:')
    else:
        print(f'不打折')
else:
#     非会员
    if money >= 200:
        print(f'打9.5折')
    else:
        print(f'不打折')

