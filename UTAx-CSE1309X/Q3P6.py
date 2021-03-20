__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


# Write a function that accepts a positive integer n as function parameter and returns True if
# n is a prime number, False otherwise. Note that zero and one are not prime numbers and two is
# the only prime number that is even.


def prime_number(n):
    output = False
    summ = 0
    if n == 0 or n == 1:
        output = False
    elif n == 2:
        output = True
    elif n > 2:
        for i in range(1,n+1):
            if n % i == 0:
                summ += i
        if summ == (n + 1):
                output = True
    else:
        ouput = False
    return output
print(prime_number(2))

