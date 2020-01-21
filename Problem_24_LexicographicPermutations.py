#A permutation is an ordered arrangement of objects. For example, 3124 is one
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
#are listed numerically or alphabetically, we call it lexicographic order. 
#The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the 
#digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time
from itertools import permutations

def get_perm_nums():
    return [[int(''.join(str(i) for i in x))] for x in permutations('0123456789',10)]

def list_of_permu_nums():
    permu_nums_list = sorted(get_perm_nums())
    millionth_num = permu_nums_list[999999]
    return millionth_num #return the millionth permutation
    

start = time.time()
millionth_num = list_of_permu_nums()
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (millionth_num,elapsed))