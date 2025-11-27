def multiply(data):
    result = 1
    for i in data:
        result *= i
    return result


x = (1, 2, 3, 4, 5)
# 系统的内置函数  min, max, sum...
math_list = [min, max, sum, multiply]
for function in math_list:
    print(function, function(x))