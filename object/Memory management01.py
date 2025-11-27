import sys


# sys.getrefcount(对象) 计数对象被引用的次数,
# sys.getrefcount(对象) 这里传参调用临时引用一次, 会在原个数基础上+1, 输出完结果又回到正常值
# 引用计数器机制:当引用次数为0, 会自动释放
# 内存管理机制 = 引用计数器机制 + 垃圾回收机制(引用计数机制解决后剩下的循环引用 用这个来解决)
class Person:
    pass


p1 = Person()  # 1
print(sys.getrefcount(p1))  # 1+1(临时引用) -1(输出完结果)
p2 = p1  # 1+1
print(sys.getrefcount(p1))  # 1+1+1(临时引用) -1(输出完结果)
del p2  # 2-1
print(sys.getrefcount(p1))  # 1+1(临时引用) -1(输出完结果)


def log(obj):
    print(sys.getrefcount(obj))  # 临时引用+1  输出完结果-1


log(p1)  # 传参+1
print(sys.getrefcount(p1))
