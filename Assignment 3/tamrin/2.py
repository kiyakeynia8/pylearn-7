import random

n = int(input())

numbers = []

while len(numbers) <= n-1:
    x = random.randint(0, 100)

    if x in numbers:
        x = random.randint(0, 100)
        numbers.append(x)

    else:
        numbers.append(x)

if len(numbers) == n:
    print(numbers)
