
#from encrypt import *

# Implement RSA decryption with the given private key p, q, exponent.



def DecipherSmallPrime(ciphertext, modulo, exponent):
    
    if small_big_prime_gen(modulo) == -1:
        return "don't know"
    else:
        p,q = small_big_prime_gen(modulo)
        return Decrypt(ciphertext, p, q, exponent)



def DecipherSmallDiff(ciphertext, modulo, exponent):
    
    
    lower_bound = IntSqrt(modulo) - 5000
    upper_bound = IntSqrt(modulo)
    
    for i in range(lower_bound, upper_bound + 1):
        if modulo % i == 0:
            p = i
            q = modulo//i
            return Decrypt(ciphertext, p, q, exponent)

    

