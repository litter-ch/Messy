# 凯撒密码
str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str1)
front3 = str1[:3]
end3 = str1[3:]
str2 = end3 + front3
# 加密文
print(str2)

str = input(f'请输入您的明文:')
len_str = len(str)  # 明文长度
print(len_str)
i = 0
# list = [] # 定义一个空列表存储索引值
encode_ = []
while i <= len_str-1:
    index_str = str1.find(str[i])  # 输入的明文索引值
    # list.append(index_str)  # 将输入的明文索引值存储在list空列表
    encode_.append(str2[index_str])  # 明文的索引值找 加密文对应的字母
    i += 1
# print(list)
print(encode_)
print(''.join(encode_))



