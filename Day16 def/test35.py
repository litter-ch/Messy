# 设计自己的 range() 函数
def my_range(*args):
    # 判断 args 有几个参数
    len_ = len(args)
    # 定义 start, stop, step 变量
    start = 0
    stop = 0
    step = 1
    # 判断
    if len_ == 1:
        stop = args[0]
    elif len_ == 2:
        start = args[0]
        stop = args[1]
    elif len_ == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        # 默认处理, 直接返回, 意味着不处理
        return
    # 正常的逻辑处理
    n = start
    while n < stop:
        # yield 关键字返回的是一个生成式对象(generator 对象)
        yield n
        # n 自增
        n += step


# range(10) 返回 0~9 之间的数值, 返回的是一个 range 对象(生成式对象 generator) 可以迭代
r1 = my_range(1, 11, 2)
print(f'{r1=}')
for i in r1:
    print(i, end=' ')
print()

r2 = my_range(10, 20)
# 生成式对象可以使用 next() 内置函数实现元素的一一获取
v1 = next(r2)
print(f'{v1=}')
v2 = next(r2)
print(f'{v2=}')
