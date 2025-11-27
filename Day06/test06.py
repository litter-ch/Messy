y = 123
for i in range(3):
    password = int(input(f'请输入密码:'))
    if password == y:
        print(f'密码正确')
        break
    else:
        print(f'密码错误,还有{2-i}次机会')
        continue
else:    # 这个else是for循环的语句块, 循环自己结束的时候执行， 而不是遇到break
        print(f'冻结账户')
print(f'结束')

