def upper_str(text):
    return text.upper()


# 调用函数
print(upper_str('heelo word'))
# 函数也是一个对象, 可以赋值给另一个变量
# 对象就是内存中的'地址'
a = upper_str
print(a('ahfuihff'))

print(f'{a= },{upper_str= }')
print(f'{type(a)=},{type(upper_str)=}')
