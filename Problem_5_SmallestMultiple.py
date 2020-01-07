num = 2
count = 0
i = 1
while count <= 20:
    if num % i == 0:
        i += 1
        count += 1
    elif count < 20:
        count = 0
        num += 2
        i = 1

print(num)
