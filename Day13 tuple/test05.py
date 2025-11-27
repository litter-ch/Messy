names = ['张三', '李四', '王五', '刘六']
scores = [98, 87, 78, 89]
x = ('sff', 'fsf', 95, 58, 52)

# zip() 压缩的操作
# 格式:zip(压缩对象)
# zip()对象的元素数量以短的作为标准
zip_object = zip(names, scores, x)
print(zip_object, type(zip_object))

# 视我们的需要将zip()对象转化成其他的类型
tuple_object = tuple(zip_object)
print(tuple_object, type(tuple_object))

# unzip() 解压缩的操作
# 格式:zip(*解压随的对象)
n1, n2, n3 = zip(*tuple_object)
print(n1, n2, n3)
