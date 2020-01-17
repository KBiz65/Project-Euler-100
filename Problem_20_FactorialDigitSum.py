#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
import time

def factorial_sum(factorial):
    ans = 1
    ans_sum = 0
    for i in range(factorial, 0, -1):
        ans *= i
        str_ans = str(ans)
    for index in range(len(str_ans)):
        ans_sum += int(str_ans[index])
    return ans_sum


start = time.time()
total_sum = factorial_sum(100)
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (total_sum,elapsed))
