list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print (list[1:3])       # 从第二个开始输出到第三个元素
# 获得结果 [786, 2.23]
print (list[1:0])       # 没有输出的值
# 获得结果 []

print (list[1:1])       # 没有输出的值
# 获得结果 []

print (list[0:1], type(list[0:1]), len(list[0:1]))       # 没有输出的值
# 获得结果 ['abcd']
print(list[0], type(list[0]))
