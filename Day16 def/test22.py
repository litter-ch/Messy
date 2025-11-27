def outer():
    print('outer running...')

    # inner() 函数实现 1~n 整型数值的累加
    def inner(n):
        print('inner running...', inner)
        return sum(range(1, n+1))
    # 函数可以作为返回值 return
    return inner


# 调用函数, 返回的结果也是一个函数
func = outer()
print(f'{func=}')

print('-' * 50)

# func() 其实调用的是inner() 函数
result = func(10)
print(f'{result=}')
