__author__ = 'Mohammad Yousuf Ali, email:aliyyousuf@gmail.com,fb.com/aliyyousuf'


# Write a function that accepts two positive integers as parameters. The first integer is the
# number of heads and the second integer is the number of legs of all the creatures in a farm
# which consists of chickens and dogs. Your function should calculate and return the number of
# chickens and number of dogs in the farm in a list as specified below. If it is impossible to
# determine the correct number of chickens and dogs with the given information then your
# function should return None.

def chicken_dog(H,L):
    chicken = []
    dogs = []
    LL = None
    if H > L:
        return None
    elif (L - (H-1) * 2) >= 2:
        for i in range(1,H):
            #if (L - (H-i)*i) >= 2:
                chicken = (H-i)*2/2
                dogs = ((L - (H-i)*2)/4)
                if chicken + dogs == H:
                    LL = [chicken] + [dogs]
                    #LL += [dogs]
        return LL
    else:
        return None
print(chicken_dog(12,34))
