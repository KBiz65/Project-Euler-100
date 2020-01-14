#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

import time

def calc_exponent(integer, exponent):
    large_num = integer**exponent
    return large_num

def sum_string(large_num):
    total_sum = 0
    for digit in range(len(str(large_num))):
        large_num_string = str(large_num)
        total_sum += int(large_num_string[digit])
    return total_sum

start = time.time()
ans = sum_string(calc_exponent(2,1000))
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (ans,elapsed))
