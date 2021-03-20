__author__ = 'Mohammad Yousuf Ali, email:aliyyousuf@gmail.com,fb.com/aliyyousuf'


# Write a function that accepts two positive integers as function parameters and returns their
# least common multiple (LCM). The LCM of two integers a and b is the smallest (non zero)
# positive integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12,
# the LCM of 10 and 5 is 10

def LCM(a,b):

    L1 = [a,b]
    min_val = min(L1)
    L2 = [ii*a for ii in range(1,min_val+1)]
    L2 += [i*b for i in range(1,min_val+1)]
    L2 = list(set(L2))

    #L3 = [k for k in L2 if k%a==0 and k%b==0]
    return min([k for k in L2 if k%a==0 and k%b==0])

print(LCM(6,4))



