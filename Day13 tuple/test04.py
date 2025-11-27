drinks = ['coffee', 'milk', 'tea']

# 解析enumerate对象
for drink in enumerate(drinks):
    print(drink, type(drink))

for count, drink in enumerate(drinks):
    print(count, drink, type(enumerate(drinks)))