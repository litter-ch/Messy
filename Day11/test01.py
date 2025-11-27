str = 'Python'
# 正值索引
print(f'{str[0]=}, {str[1]=}, {str[2]=}')
# 负值索引
print(f'{str[-1]=}, {str[-2]=}, {str[-3]=}')

# 多重定义的观念
s1, s2, s3, s4, s5, s6 = str
print(s1, s2, s3, s4, s5, s6)

# 字符序列的切片
print(f'{str[0:3]=}')
print(f'{str[3:]=}')
print(f'{str[::2]=}')

# 字符序列的最值和长度
print(f'{len(str)=}')
print(f'{max(str)=},Unicode码值为{ord(max(str))}')
print(f'{min(str)=},Unicode码值为{ord(min(str))}')


