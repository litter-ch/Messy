names1 = '张三 李四 王五 刘六'

# 切割字符串
# 格式:对象.split(分隔符)   返回的是一个列表
# 用分隔符将字符串拆开成列表 没有指定分隔符则默认为空格
name_list1 = names1.split()
print(name_list1)

names2 = '张三#李四#王五#刘六'

name_list2 = names2.split('2')
print(name_list2)
name_list2 = names2.split('#')
print(name_list2)
