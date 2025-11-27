import random
import math
x = random.randint(1,100)
y = random.randint(1,100)
print(f'x={x},y={y}')
min_ = min(x, y)
max_ = max(x, y)
result = 0
while min_ <= max_:
    if min_ % 2 == 0:
        print(min_, end='\t')
    result += min_
    min_ += 1
print(f'result=', result, end='\t')
