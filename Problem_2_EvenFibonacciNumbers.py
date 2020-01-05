#Project Euler #2 / Even Fibonacci Numbers

sum = 0
fib_current = 1
fib_next = 2

while sum <= 4000000:
    if fib_current % 2 == 0:
        sum += fib_current
        fib_current, fib_next = fib_next, fib_current + fib_next
    else:
        fib_current, fib_next = fib_next, fib_current + fib_next


print(sum)
