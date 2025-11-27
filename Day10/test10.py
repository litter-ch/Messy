# 整型列表
numbers1 = [7, 3, 6, 2, 8, 4, 9, 5]
numbers2 = [7, 3, 6, 2, 8, 4, 9, 5]

# 升幂排序(从小到大)   格式:对象.sort()
numbers1.sort()
print(f'{numbers1=}')

# 降幂排序(从大到小)
numbers1.reverse()  # 需要先进行排序,再进行颠倒
numbers2.sort(reverse=True)  # 可以直接将无序的进行降幂排序  格式:对象.sort(reverse=True)
print(f'要先在前面进行升幂排序再颠倒实现降幂排序的{numbers1=}')
print(f'直接进行降幂排序的{numbers2=}')




