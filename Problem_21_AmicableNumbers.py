#Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
#each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
#142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

import time

def get_factor_sum(factor):
    i = 2
    factor_sum = 0
    while i*i <= factor:
        if factor % i == 0:
            factor_sum += i + (factor // i)
        i += 1
    return(factor_sum + 1)

def find_amicable_nums():
    total_sum = 0
    dict_sums = {}
    for i in range(2, 10000):
        num_fact_sum = get_factor_sum(i)
        if num_fact_sum == i:
            continue
        dict_sums[i] = num_fact_sum
        if num_fact_sum in dict_sums:
            if (i == dict_sums[num_fact_sum]) and\
            (num_fact_sum == dict_sums[i]):
                total_sum += num_fact_sum + i
            else:
                dict_sums[num_fact_sum] = get_factor_sum(num_fact_sum)
                if (i == dict_sums[num_fact_sum]) and\
                (num_fact_sum == dict_sums[i]):
                    total_sum += num_fact_sum + i
    return total_sum


start = time.time()
total_sum = find_amicable_nums()
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (total_sum,elapsed))
