str1 = 'abc'
# 发送方将字符串(编码)成字节进行传输  接收方将字节(译码)成字符串
# 网络中通用的编码格式 'utf-8'
encode1_name = str1.encode('utf-8')  # utf-8将一个英文编译成一个字节
print(encode1_name, len(encode1_name))

# 格式:对象.encode(字符集)    编码  作用是将字符串数据类型转换为'二进制字节数据类型'
# 如果字符集不指定,则默认为utf-8
str2 = "中国"  # utf-8将一个中文编译成三个字节
encode2_name = str2.encode('utf-8')
print(encode2_name, len(encode2_name))

# 格式:对象.decode(字符集)    译码  作用是将二进制字节数据转化为指定字符集的字符串数据
str3 = encode2_name.decode('utf-8')
print(str3, len(str3))

