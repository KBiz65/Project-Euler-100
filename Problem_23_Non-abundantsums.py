#A perfect number is a number for which the sum of its proper divisors is
#exactly equal to the number. For example, the sum of the proper divisors of 28
#would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than
#n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
#number that can be written as the sum of two abundant numbers is 24. By
#mathematical analysis, it can be shown that all integers greater than 28123
#can be written as the sum of two abundant numbers. However, this upper limit
#cannot be reduced any further by analysis even though it is known that the
#greatest number that cannot be expressed as the sum of two abundant numbers is
#less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum
# f two abundant numbers.

import time

def create_abundant_nums_list():
    abundant_nums_list = []

    for i in range(1, 28124):
        num_check = get_factors(i)
        if num_check > 0:
            abundant_nums_list.append(num_check)

    return abundant_nums_list

def get_factors(number):
    i = 2
    factors_list = [1]
    while i*i <= factor:
        if factor % i == 0:
           factors_list.append(i)
           factors_list.append(number // i)
        i += 1
    abundant_num = sum(factors_list)
        
    return abundant_num

start = time.time()
total_score = get_names_score('Problem_22_namesfile.txt')
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (total_score,elapsed))