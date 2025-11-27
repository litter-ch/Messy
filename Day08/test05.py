result = input("请输入数值公式:")
print(result)
# eval()函数 处理字符串进行解析 实现数值运算
result = eval(result)
print(result)
print(f'计算结果为:{result:8.2f}')

# 多变量输入
n1, n2, n3 = eval(input("请输入三个数字(并用英文逗号分隔):"))
print(n1, n2, n3)

# 直接解析字符串, 并执行对应的程序
eval('print("hello world")')