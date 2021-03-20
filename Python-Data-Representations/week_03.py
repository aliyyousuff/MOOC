__author__= "aliyyousuf@gmail.com"




# Question: 06

# Given a list fib = [0, 1], write a loop that appends the sum of the last two
# items in fib to the end of fib. What is the value of the last item in fib after
# twenty iterations of this loop? Enter the answer below as an integer.

fib = [0,1]

itr = 20

for i in range(itr):
    fib.append(sum(fib[len(fib)-2:]))

#print(fib[-1])


# Question 07:

def eratosthens(upperBound):

    '''In mathematics, the sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit.'''

    numbers = list(range(2,upperBound + 1))

    for n in numbers:
        for m in numbers:
            if m > n:
                if m % n == 0:
                    numbers.remove(m)
                else:
                    pass
            else:
                pass
    return len(numbers)

