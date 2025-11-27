stus = {'张三', '李四', '王五', '刘六', '貂蝉', '杨玉环', '王昭君', '西施', '刘德华', '黎明', '郭富城', '张学友'}

# 参加数学夏令营的人员
math = {'张三', '刘德华', '西施', '貂蝉'}
# 参加物理夏令营的人员
physics = {'张三', '王五', '杨玉环', '张学友', '貂蝉'}
# 参加英语夏令营的人员
english = {'王五', '刘六', '王昭君', '黎明', '郭富城'}

#
result1 = math & english
print(result1, len(result1))

result2 = math & physics
print(result2, len(result2))

result3 = stus - (math | physics | english)
print(result3, len(result3))