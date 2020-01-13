import time
#What is the value of the first triangle number to have over five
#hundred divisors?
def calc_tri_num(tri_num, count):
    tri_num += count
    return tri_num

def get_num_factors(factor):
    i = 1
    factor_count = 0
    while i*i <= factor:
        if factor % i == 0:
            factor_count += 1
            if factor//i != i:
                factor_count +=1
        i += 1
    return factor_count

def find_factors(factors_needed):
    count = 1
    tri_num = calc_tri_num(0, count)
    tri_num_factors = 0
    if tri_num == 1:
        count += 1
        tri_num = calc_tri_num(tri_num, count)
    while tri_num_factors < factors_needed:
        tri_num_factors = get_num_factors(tri_num)
        count += 1
        if tri_num_factors > factors_needed:
            return tri_num
        else:
            tri_num = calc_tri_num(tri_num, count)

start = time.time()
triangle_number = find_factors(500)
elapsed = (time.time() - start)

print("result %s returned in %s seconds." % (triangle_number,elapsed))
