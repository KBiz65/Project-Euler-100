#Starting in the top left corner of a 2×2 grid, and only being able to move to
#the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

#setting up the size a 20x20 grid would be

import time

def find_path_options(row, col):

    total_steps = row + col
    numerator = 1
    denominator = 1

    for i in range(total_steps, 0, -1):
        if i > row:
            numerator *= i
        if i <= row:
            denominator *= i

    return numerator / denominator


start = time.time()
print(find_path_options(20,20))
elapsed = (time.time() - start)
print("result returned in %s seconds." % (elapsed))
