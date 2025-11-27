name1 = '玛丽亚'  # 字符串型
print(name1)
print(f'玛丽亚={name1},type(name1) = {type(name1)}')
x = 5  # 整型
print(x)
num2 = 66.6  # 浮点型
print(f'num2={num2},type(num2) = {type(num2)}')
is_visited = True  # 布尔型
print(f'is_visited={is_visited},type(is_visited) = {type(is_visited)}')
# 列表数据类型 有序 可重复 可扩展
name3 = ['张三', '李四', '刘五', '张三']
print(f'name3 = {name3},type(name3) = {type(name3)}')
# 元组数据类型 有序 可重复 不可扩展
name3 = ('张三', '李四', '刘五', '张三')
print(f'name3 = {name3},type(name3) = {type(name3)}')
print(len(name3))
# 集合类型 无序(内部通过一套算法实现的，可能使用了当前时间戳变量) 不可重复 可扩展
name3 = {'张三', '李四', '刘五', '张三'}
print(f'name3 = {name3},type(name3) = {type(name3)}')
# 字典类型 :key->value  键值对/夫妻对 dict =>dictionary
stu_dict = {'stu_id': '20203524', 'name': '谢俊峰', 'age': '22', 'score': '100'}
print(f'stu_dict = {stu_dict},type(stu_dict) = {type(stu_dict)}')
a = set('sguagufgi')  # 集合函数
b = set('sibghk')
print(f'a = {a},type(a) = {type(a)}')
print(f'b = {b},type(b) = {type(b)}')
print(a | b)  # 并集合
print(a & b)  # 交集合
print(a - b)  # a集合与b集合的差
print(b - a)  # b集合与a集合的差
print(a ^ b)  # 并集-交集（没有同时存在的元素）
