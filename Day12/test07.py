# 生成1~10整数存储到列表中
list1 = []
for i in range(1, 11):
    list1.append(i)
print(f'{list1=}')

# list() 类型转换
list2 = list(range(1, 11))
print(f'{list2=}')

# 生成器 generator 来实现
list3 = [i for i in range(1, 11)]
print(f'{list3=}')

# 需求: 添加1~10的平方数
list4 = [pow(i, 2) for i in range(1, 10)]
print(f'{list4=}')

# 将摄氏温度转换为华氏温度
celsius = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = [(c * 9 / 5 + 32) for c in celsius]
print(f'{fahrenheit=}')
