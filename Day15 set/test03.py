numbers = {1, 2, 3, 4, 5}
print(numbers)

# 添加元素
numbers.add(6)
print(numbers)

# 删除元素  删除时, 如果元素不存在会报错
numbers.remove(6)
print(numbers)

# discard()  可以删除元素 如果元素不存在不会报错
numbers.discard(1)
print(numbers)

# pop() 弹出最后一个元素, 由于集合的无序性, 相当于随机删除
element_pop = numbers.pop()
print(numbers, element_pop)

# clear() 清除集合中所有的元素, 但集合还存在 为{}, 后续可以继续添加元素
result = numbers.clear()
print(f'{result=},{numbers=}')
