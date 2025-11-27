# 穷举 : 一个一个数 语法:while True +if 判断 + break 跳出
i = 2
while 1:
    if i % 2 == 1 \
    and i % 3 == 1 \
    and i % 4 == 1:
        print(i)
        break
    i += 1
