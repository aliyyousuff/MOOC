__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


# Write a function named crazy_list that accepts a list as parameter and returns a boolean
# (either True or False) based on whether or not the list is the same forward and backwards.
# You may NOT use list.reverse() method.
# For example, if the list received by the function is:

#[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
# (Notice how the list is exactly the same whethere you read it from left to right,
# or from right to left) Then your function should return the Boolean
# True
#however, if the list recieved by the function is something like this:
#[4, 5, 6, 7, 8, 4, 5, 2]
#(Notice how the list is NOT the same when reading from left to right vs right to left)
# In this case, your function should return the Boolean


def crazy_list(L):

    count = 0
    last = False

    if len(L) %2 != 0:
        f1 = L[0:int(len(L)/2)+1]
        f2 = L[int(len(L)/2):]
        for chr1,chr2 in zip(f1,f2[::-1]):
            if chr1 == chr2:
                count += 1
                #print(chr1,chr2)
        if count == (len(f1)):
            return True
        else:
            return False

    if len(L) % 2 == 0:
        f2 = L[int(len(L)/2):len(L)]
        for chr1,chr2 in zip(L[:len(L)+1],f2[::-1]):
            if chr1 == chr2:
                 count += 1
        if count == len(f2):
            return True
        else:
            return False


LE = [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]



LE2 = [4, 5, 6, 7, 8, 4, 5, 2]
print(crazy_list(LE2))


