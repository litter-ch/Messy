# 简单面向对象概念
s = 'abc'
# 需求:查看字符串对象的内部函数/方法
print(dir(s))
# 需求:查看具体内部函数/方法的详细说明
print(help(s.isalpha))

n = 123
print(dir(n))
print(help(n.bit_length))