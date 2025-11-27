vip_names = ['Jack', 'Peter', 'Tom', 'Jerry', 'Lucy']
# 循环 遍历/迭代 列表中的每一个元素
# for 变量名称 in 可迭代对象:

# 方法1
for vip in vip_names:
    print(vip, end=' ')
print()

# 方法2
print(' '.join(vip_names))


# len_vip_names = len(vip_names)
# i = 0
# while i <= len_vip_names - 1:
#     print(vip_names[i])
#     i += 1
