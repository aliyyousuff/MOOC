__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

# Write a function that receives a positive integer as function parameter and returns True if
# the integer is a perfect number, False otherwise. A perfect number is a number whose sum of
# the all the divisors (excluding itself) is equal to itself. For example: divisors of 6
# (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number.
def common_divisor(n):
    output = False
    summ = 0
    for i in range(1,n):
        if n % i == 0:
            summ += i
    if summ == n:
        output = True
    return output


