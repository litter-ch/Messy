# 整型列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 切片的语法格式 [start:end:step]
# 输出不包括下标为end
# 从start开始(不指定start则默认下标为0), 到end(不指定end则默认为下标为列表长度)

# 需求1: 输出前5个元素
print(f'前五个元素:{numbers[:5]}')

# 需求2: 输出所有奇数
print(f'奇数:{numbers[::2]}')
# 负数下标(从后向前)
print(numbers[-1])