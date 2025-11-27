# 正方形
for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        print(f'*', end='  ')
    print()

# 直角三角形
for i in range(5):
    for j in range(i+1):
        print(f'*', end='')
    print()

# 倒三角形
for i in range(5):
    for j in range(5-i):
        print(f'*', end='')
    print()
#
for i in range(10):
    if i < 5:
        for j in range(i):
            print(f'*',end='')
        print()
    else:
        for j in range(10-i):
            print(f'*',end='')
        print()
