first_list = []
last_list = []

while True:
    a = int(input())

    if a == 987:
       break
    else:
        first_list.append(a)

for number in first_list:
    if number not in last_list:
        last_list.append(number)
print(last_list)