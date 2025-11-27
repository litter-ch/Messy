my_sport = ['fitness', 'swimming', 'reading']
# 列表的直接赋值, 意味着两个列表指向的是内存的同一块空间  一个列表更改元素会影响到另一个列表同步更改
friend_sport = my_sport
print(f'{friend_sport=},   {my_sport=}')
print(f'{id(my_sport)=},   {id(friend_sport)=}')

friend_sport.append('running')
print(f'{friend_sport=}, {my_sport=}')

print('-'*50)

my_class = ['chinese', 'math', 'english', 'music']
# 列表的切片复制(两块不同的内存空间)    一个列表更改元素不会影响到另一个列表
friend_class = my_class[:]
print(f'{my_class=}, {friend_class=}')
print(f'{id(my_class)=}, {id(friend_class)=}')
friend_class.append('sport')
print(f'{my_class=}, {friend_class=}')

