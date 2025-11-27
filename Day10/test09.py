# 颠倒排序
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用切片实现列表元素的颠倒, 不会改变原列表
# 会返回一个新列表, 需要去接受
numbers2 = numbers1[::-1]
print(f'{numbers1=}\n{numbers2=}')

# 使用reverse()方法实现列表的颠倒, 将原列表改变
# 不用去接收, 接受会返回None(未定义,不存在)
# 格式:对象.reverse()
numbers1.reverse()
numbers3 = numbers2.reverse()
print(f'{numbers1=}\n{numbers2=}\n{numbers3=}')
