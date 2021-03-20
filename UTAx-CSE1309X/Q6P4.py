__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'



# Write a function named formatted_output that receives a dictionary as argument. The keys of the dictionary will be the names of the students and the values of the dictionary will be their average scores. Your function should print this information exactly as specified below :

# For example if the dictionary received by the function is

#   {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}
# Then your function should print:


#  alex       90.55
#  eva        88.50
#  tim        65.90
#  john       34.48



def formatted_print(D):

    from collections import OrderedDict
    from operator import itemgetter
    D = OrderedDict(sorted(D.items(), key=itemgetter(1), reverse=True)) # sorting Dict by values at reverse order.
    for k, v in D.items():
        print('{0:<10s} {1:>5.2f}'.format(k,v))