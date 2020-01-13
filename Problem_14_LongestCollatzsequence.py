#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains
#10 terms. Although it has not been proved yet (Collatz Problem), it is thought
#that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?

import time
start = time.time()

def get_chain_length(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num//2
            count += 1
        else:
            num = (3 * num) + 1
            count += 1
    return count

longest_num = 0
longest_num_count = 0

for i in range(2, 1000000):
    longest_count = get_chain_length(i)
    if longest_count > longest_num_count:
        longest_num_count = longest_count
        longest_num = i

elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (longest_num, elapsed))
