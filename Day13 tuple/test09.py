# 解包
x, y = (10, 20)
print(x, y)

# 多重打包
a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)

[a, b, c] = (1, 2, 3)
print(a, b, c)

[a, [b, c]] = [1, (2, 3)]
print(a, b, c)

x = ('张三', (90, 95))
print(f'姓名:{x[0]}, 语文成绩:{x[1][0]}, 数学:{x[1][1]}')

(name, (chinese, math)) = ('张三', (90, 95))
print(name, chinese, math)