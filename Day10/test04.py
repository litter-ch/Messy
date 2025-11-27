numbers = [88, 66, 33, 99, 22, 11, 77, 55, 44]
# 最大值 max()
print(f'最大元素为:{max(numbers)}')
# 最小值 min()
print(f'最小元素为:{min(numbers)}')
# 列表中整型元素的总和 sum()
print(f'元素总和为:{sum(numbers)}')
# 列表中的元素个数 len()
print(f'元素个数为:{len(numbers)}')

scores = ['张三', 99.3, 59, 88]
# 最值 只能数值类型进行比较 用切片选择数值类型
print(f'最高分为:{max(scores[1:])}')

# 将列表的元素实现修改
print(scores)
scores[1] = 87
print(scores)
scores[0], scores[1], scores[2], scores[3] = '李四', 100, 57, 66
print(scores)
