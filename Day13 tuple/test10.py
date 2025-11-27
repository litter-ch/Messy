x = [1, 3, 5, 7, 9]
# 将列表数据转换成 bytes 二进制数据 (不可修改, 类似于元组)
x_bytes = bytes(x)
print(x_bytes, type(x_bytes))

# TypeError: 'bytes' object does not support item assignment
# x_bytes[0] = 10  会报错

for i in x_bytes:
    print(i)

y = [1, 3, 5, 7, 9]
# 将列表数据转换成 bytearray 二进制数据 (可修改, 类似于列表)
y_bytearray = bytearray(y)
print(y_bytearray, type(y_bytearray))

# 修改二进制类型中的元素
y_bytearray[0] = 10

for i in y_bytearray:
    print(i)
