# 高阶函数
# filter(func, iterable)
# map(func, iterable)
# reduce(func, iterable)
# func : 传递一个函数
# iterable : 传递一个可迭代对象

numbers = [i for i in range(1, 21)]
# filter() 过滤器函数      将 iterable 中满足 func 的留下来
result = filter(lambda x: x % 3 == 0, numbers)
print(list(result))

# map(func, iterable) 映射函数
result = map(lambda x: pow(x, 2), numbers)
print(list(result))



