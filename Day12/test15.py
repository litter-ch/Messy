numbers = list(range(1,10))
print(numbers)
index = -1
while True:
    index += 1
    if index == len(numbers):
        break
    number = numbers[index]
    if number % 2:
        continue
    print(number)
