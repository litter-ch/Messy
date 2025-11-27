# 简单面向对象概念
# 格式化字符串位置
title = '图灵Python学习之旅'
print(title)
# 居中, 指定宽度,并且可以指定填充字符,如果不指定,默认填充字符为空格
# 格式: 对象.center(宽度,字符)
title2 = title.center(50, '-')
print(f'/{title2}/')

# 左对齐 格式:对象.ljust(宽度,字符)
title3 = title.ljust(50, '-')
print(f'/{title3}/')

# 右对齐 格式:对象.rjust(宽度,字符)
title4 = title.rjust(50)
print(f'/{title4}/')

# 右对齐 格式:对象.zfill(宽度) 使用0实现填充
title5 = title.zfill(50)
print(f'/{title5}/')