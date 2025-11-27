url = "http://www.baidu.com/json?city="
city = 'beijing'
r = 1000
type = 'school'
print('{}{}&radius={}&type={}'.format(url, city, r, type))
print(f'{url}{city}&radius={r}&type={type}')

title = "你好"

print("/{0:^20s}/".format(title))
print("/{0:*^20s}/".format(title))
# *会将空格进行填充

x = 666
print(f'x={x}')
print(f'{x=}')
print(f'{x=: ^10d}')