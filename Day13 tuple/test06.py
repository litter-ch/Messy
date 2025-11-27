nums = (i for i in range(10))
print(nums, type(nums))

# 遍历就是生成式的第一次使用
for num in nums:
    print(num)

# 将生成式转成列表
# 生成式不能使用第二次, 如果使用第二次, 则没有任何元素可以取得
list_nums = list(nums)
print(list_nums)

stu_no = ('stu' + str(i) for i in range(10))
# 这是生成式的第一次使用
stu_list = list(stu_no)
print(stu_list)

# 第二次使用
stu_tuple = tuple(stu_no)
print(stu_tuple)