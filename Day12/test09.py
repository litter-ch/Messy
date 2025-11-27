# 添加 1~100 之间可以被 7 整除的数值

# 方法1
list1 = []
for i in range(101):
    if i % 7 == 0:
        list1.append(i)
        i += 1
print(f'{list1=}')

# 方法2
# 进阶语法的简写
list2 = [i for i in range(101) if i % 7 == 0]
print(f'{list2=}')


