__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



# Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD). Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples:

# if the list was [12, 24, 6, 18]
# then your function should return the GCD: 6
# if the list was: [3, 5, 9, 11, 13]
# then your function should return their GCD: 1

def find_integer_with_most_divisors(L):

    import collections
    import operator
    import functools
    D = collections.OrderedDict()

    for i in L:
        LL = []
        for ii in range(1,i+1):
            for iii in range(1,i+1):
                if ii * iii == i:
                    LL += [ii]
        D[i] = set(LL)

    T =  max(functools.reduce(operator.and_,D.values()))

    if T:
        return T
    else:
        return 1

k = [12, 18, 6, 21]
print(find_integer_with_most_divisors(k))