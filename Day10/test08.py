# 列表的长度是可伸缩的
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 拼接    格式:列表名.append(元素)
numbers.append(11)
print(numbers)

# 在指定的下标位置插入指定元素   格式:列表名.insert(下标,元素)
numbers.insert(0, 0)
print(numbers)

# 删除
# 不知道元素,用pop方法删除指定下标的元素   系统会返回这个元素告诉你
# 格式:对象.pop(下标)  不指定下标则默认最后一个元素
numbers.pop(0)
delete_numbers = numbers.pop(0)
print(numbers)
print(f'被删除的元素为:{delete_numbers}')

# 知道元素,不知道元素在列表中的下标 用remove删除
# 因为知道元素  系统不会返回这个元素来告诉你
# 格式: 对象.remove(元素)
numbers.remove(5)
print(numbers)
z