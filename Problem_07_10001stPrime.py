def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = 2
count = 0
prime_nums = []

while count <= 10001:
    if is_prime(n):
        prime_nums.append(n)
        count += 1
        n += 1
    else:
        n += 1

print(prime_nums[-2])
