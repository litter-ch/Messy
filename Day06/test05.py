#    循环控制语句 : break 跳出'当前'循环

while True:
    choice = input('去不去？(去y/不去n):')
    if choice == 'y' or choice == 'Y':
        print('go!')
        break # 循环一旦遇到break就会跳出当前的循环
    else:
        print('啊?')

#     循环结构语句 continue
#     结束本次循环,继续下次循环

for i in range(10):
    if i == 5:
        continue # 循环后面的代码就不执行了, 回到循环条件, 执行下一趟

    print(i, end='\t')
# break往循环外面跳   continue往循环的条件位置跳继续下一个循环
