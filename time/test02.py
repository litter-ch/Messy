import time
'''
    %y 两位数的年份表示 (00-99)
    %Y 四位数的年份表示 (000-9999)
    %m 月份 (01-12)
    %d 月内的一天 (01-31)
    %H 24小时制小时数(0-23)
    %I 12小时制小时数(01-12)
    %M 分钟数(00-59)
    %S 秒(00-59)
'''

# 时间元组->格式化日期   time.strftime(格式化字符串, 时间元组)
result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(result)

# 格式化日期->时间元组   time.strptime(日期字符串, 格式化字符串)
pt = time.strptime(result, "%Y-%m-%d %H:%M:%S")
print(pt)

# 时间元组->时间戳       time.mktime(时间元组)
t = time.mktime(pt)
print(t)

