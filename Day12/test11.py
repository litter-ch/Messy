# 列出ASCII/Unicode码值

list_ = [chr(i) for i in range(128)]
print(list)

for i in range(128):
    print(chr(i), end=' ')

for i in range(0x6d2a, 0x6e2a):
    print(chr(i), end=' ')