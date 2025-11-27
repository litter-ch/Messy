money = 0
count = 0
while money <= 200:
    if money < 100:
        money += 5.4 * 0.9
    else:
        money += 5.4 * 0.7
    count += 1
print(money)
day = count / 2
print(int(day))
