n = eval(input(f'Enter a number:'))
sum_ = sum(range(n+1))
print(sum_)

# 获取 10 之内整型数值的平方
if n > 10: n = 10  # 限制 n 在 10 范围内

sum_ = 0
squares = []
for i in range(1, n+1):
    pow_ = pow(i, 2)
    squares.append(pow_)
    sum_ += pow_
print(squares)
print(sum_)



