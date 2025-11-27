stu_no = ['stu_' + str(i) for i in range(1, 6)]
names = ['张三', '李四', '王五', '刘六', '杨七']

stu_dict = dict(zip(stu_no, names))
print(stu_dict)

# get() 根据key 获取对应的value  如果不存在 则返回None
# 格式:字典.get(key键)
name = stu_dict.get('stu_2')
print(name)
name = stu_dict.get('stu_10', 'NOT EXIST')   # 设置返回的默认值
print(name)

# fromkeys() 将列表转换为字典
# 格式:dict.fromkeys(列表, value值)  不指定value值, 则默认None
list_dict1 = dict.fromkeys(names)
print(list_dict1)
list_dict2 = dict.fromkeys(names, 'value值')
print(list_dict2)

# setdefault() 添加新数据
# 如果 key 存在, 则不影响数据
# 格式:字典.setdefault(key键, value值)
stu_dict.setdefault('key键', 'value值')
print(stu_dict)
