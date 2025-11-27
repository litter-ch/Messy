import time

# 时间戳
result = time.time()
# 当前年份
years = result / (24 * 60 * 60 * 365) + 1970
print(years)
print(result)

# 时间元组
result = time.localtime()
print(result)

# time.sleep(secs) 推迟线程的执行, 让程序以 secs 秒为间隔执行
while True:
    result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(result)
    time.sleep(1)
