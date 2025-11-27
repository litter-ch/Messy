drinks = ['water', 'tea', 'coffee']
for drink in enumerate(drinks):
    print(drink)

print('-'*20)

for drink in enumerate(drinks, start=1):
    print(drink)

print('-'*20)

for count, drink in enumerate(drinks, start=1):
    print(f'{count=}, {drink=}')