# People's Republic of China  国际上的缩写:PRC
countries1 = ['Britain', 'America', 'France',
              'Spain', 'Germany', 'Switzerland',
              'Italy', 'Sweden', 'China']

# 字符中的排序根据ASCII码实现的排序
countries1.sort()
print(f'{countries1=}')

countries2 = ['America', 'Spain', 'Britain',
              'France', 'Italy',  'Germany',
              'China', 'Switzerland', 'Sweden']
# 不改变原列表的序列,创建一个新的排好序的列表
sorted_countries2 = sorted(countries2)
reversed_countries2 = sorted(countries2, reverse=True)
print(f'{countries2=}')
print(f'{sorted_countries2=}')
print(f'{reversed_countries2=}')
