# ASCII码: A->65  a->97  '0'->48
# chr()内置函数执行数据的转换 回传Unicode码值 ASCII码值所对应的字符
S1 = 65
S2 = 97
S3 = 48
print(S1, S2, S3)
print(chr(S1), chr(S2), chr(S3))

# Unicode码 所有的文字皆有一个码值 目前使用16位定义文字
# 定义方式以\u开头 后面4个十六进制数.从\u0000~\uFFFF
# 前128个码值保留给ASCII码使用
# ord()内置函数 回传函数字符的Unicode码值
s4 = '峰'
print(ord(s4))
