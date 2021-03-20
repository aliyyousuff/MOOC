# Implementation of fast modular exponentiation

def FastModularExponentiation(b, e, m):
    binary = bin(e)[2:]
    binary = binary[::-1]
    r = 1
    x = b
    for i in binary:
        if i == '1':
            r = (r * x) % m
            x = (x ** 2 ) % m
        else:
            x = (x ** 2) % m
    return r

    

        
        


    