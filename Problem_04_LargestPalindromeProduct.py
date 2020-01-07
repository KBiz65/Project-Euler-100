def is_palindrome(product):
    if product == product[::-1]:
        return True
    else:
        return False

ans = [100, 100]
product = int(ans[0] * ans[1])

for num1 in range(100,999):
    for num2 in range(100,999):
        if (num1 ** 2) > product and is_palindrome(str(num1 ** 2)) == True:
            ans[0] = num1
            ans[1] = num1
            product = int(ans[0] * ans[1])
        if (num1 * num2) > product and is_palindrome(str(num1 * num2)) == True:
            ans[0] = num1
            ans[1] = num2
            product = int(ans[0] * ans[1])
        if (num2 ** 2) > product and is_palindrome(str(num2 ** 2)) == True:
            ans[0] = num2
            ans[1] = num2
            product = int(ans[0] * ans[1])
print(product)
