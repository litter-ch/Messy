class Person:
    def __init__(self):
        self.result = 1

    # 将对象变为可迭代对象, 可以遍历(要返回next方法)
    def __iter__(self):
        self.age = 1  # 初始化迭代器对象, 使得不满足下面的抛出异常条件, 可以重复迭代
        return self

    # 将可迭代对象里的元素逐个取出来
    def __next__(self):
        self.result += 1
        if self.result >= 6:
            # 抛出异常 跳出循环
            raise StopIteration('停止遍历')
        return self.result
    # 同时满足__iter__和__next__才变为迭代器


# iter() 在外部将对象变为迭代器, 然后因为是迭代器在内部实现了__next__方法, 所以可以for in 遍历
p = Person()
for i in p:  # 除了__getitem__, 要实现for in 遍历离不开__next__方法, 相当于直接将next方法逐个取出变为一次全部取出
    print(i)

from collections.abc import Iterator, Iterable

print(isinstance(p, Iterator))  # 判断是否为迭代器
print(isinstance(p, Iterable))  # 判断是否为可迭代对象
# print(next(p))

