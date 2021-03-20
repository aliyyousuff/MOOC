__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



# Write a function called pattern_sum that receives two single digit positive integers, (k and m) as
# parameters and calculates and returns the total sum as:
# k + kk + kkk + .... (the last number in the squence should have m digits)
# For example if the two integers are:  (4, 5)
# Your function should return the total sum of:
# 4 + 44 + 444 + 4444 + 44444
# Notice the last number in this sequence has 5 digits. The return value should be: 49380

def pattern_sum(a,b):
    L1 = [x*str(a) for x in range(1,b+1)]
    L2 = [int(x) for x in L1]
    return sum(L2)
