# 模块导入
from functools import reduce

numbers = [5, 8, 6, 9, 4, 1]
# reduce(func, iterable)  缩减函数
# 拿前面两个元素执行函数, 得到结果再与第三个元素执行函数, 以此类推完所有元素
result1 = reduce(lambda x, y: x if x > y else y, numbers)
print(f'{result1=}')

result2 = reduce(lambda x, y: x + y, numbers)
print(f'{result2=}')
