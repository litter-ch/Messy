score = 90
name = "Jack"
count = 1

print("{}你的第{}次Python考试成绩是{}".format(name, count, score))
print("{0}你的第{1}次Python考试成绩是{2}".format(name, count, score))
# {}占位符开始的下标从0开始
print("{n}你的第{c}次Python考试成绩是{s}".format(n=name, c=count, s=score))

r = 5
PI = 3.1415926
area = PI * r * r
print("/半径{0:3d}圆的面积是{1:10.2f}/".format(r, area))
print("/半径{0:>3d}圆的面积是{1:>10.2f}/".format(r, area))
print("/半径{0:<3d}圆的面积是{1:<10.2f}/".format(r, area))
print("/半径{0:^3d}圆的面积是{1:^10.2f}/".format(r, area))
# >靠右对其 <左对齐 ^居中


