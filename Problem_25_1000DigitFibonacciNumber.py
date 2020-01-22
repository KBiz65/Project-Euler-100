import time

def fib_1000_digit_num():
    a, b = 0, 1
    fib_index = 0
    while len(str(a)) < 1000:
        a, b = b, a + b
        fib_index += 1
    return fib_index

start = time.time()
index = fib_1000_digit_num()
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (index, elapsed))