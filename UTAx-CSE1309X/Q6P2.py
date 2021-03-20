__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'


# Write a function named list_to_tuples that receives a two dimensional list of
# strings as parameter and returns a tuple of tuples where the content of each inner
# list is reversed as shown below: For example if the two dimensional list received
# by the function is

# [['mean', 'really', 'is', 'jean'],
# ['world', 'my', 'rocks', 'python']]
# Then, your function should return a tuple of tuples as shown below:
# (('jean', 'is', 'really', 'mean'), ('python', 'rocks', 'my', 'world'))



def list_to_tuples(L):
    return tuple([tuple(i[::-1]) for i in L])