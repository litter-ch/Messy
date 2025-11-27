'''
Python的内置函数:range(start,stop,step)
作用:生成指定范围的序列. 序列 多个数值: 1,2,3,4,5,6...这个整体称为序列.
while循环想生成一个[1,2,3,4,...,10]序列。
1. i = 1                可以用range函数的start 指定
2. while i <= 10:       可以用range函数的stop  指定(不包含)  左开右闭
3. i += 1               可以用range函数的step  指定(步数)
start 开始的数值(默认为0)
stop 结束的数值(不包含该数值) 必须指定
step 步长(默认为1)
'''

# 想生成一个[1,2,3,...,10]序列
r = range(1, 11, 1)
print(f'r={r}')

# 需求: 想查看range函数生成序列中的每一个数值
# 格式: for 循环变量 in range函数
for i in range(1, 11, 1):
    print(i, end='\t')
