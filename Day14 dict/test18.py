abc = 'abcdefghijklmnopqrstuvwxyz'
sub_text = abc[3:] + abc[:3]

encryption_dict = dict(zip(abc, sub_text))
print(encryption_dict)

message = input('输入:')

# 密文列表
cipher = []
for key in message:
    value = encryption_dict[key]
    cipher.append(value)

# 密文列表转换为字符串类型
cipher_text = ''.join(cipher)
print(cipher_text)

