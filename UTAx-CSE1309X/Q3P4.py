__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


# Write a function that accepts a list of integers as parameter
# Your function should return the sum of all the odd numbers in
# the list. If there are no odd numbers in the list, your function
# should return 0 as the sum.

def sm(l):
    s = 0
    for i in l:
        if i % 2 != 0:
            s +=  i
    return s
