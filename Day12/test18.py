# 死循环(无限循环)
while True:
    pass

while 1:
    pass

# pass 语句
schools = ['清华', '北大', '交大', '复旦', '浙大']
for school in schools:
    # 处理逻辑, 此刻还未确定如何处理
    # 加pass防止下面要执行的因为报错看不了, 后续确定如何处理再把pass换掉
    pass
