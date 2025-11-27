# for-else语句  如果全都执行完毕了也没有满足结果, 执行else 语句
# 测试某个大于 2 的整数是否为质数
numbers = eval(input(f'请输入整数:'))
for num in range(2, numbers):
    if numbers % num == 0:
        print(f'{numbers}不是质数')
        break
else:
    print(f'{numbers}是质数')
