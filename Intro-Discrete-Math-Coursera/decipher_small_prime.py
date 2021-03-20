#from encrypt import *

# Implement RSA decryption with the given private key p, q, exponent.


def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res


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


def Encrypt(message, modulo, exponent):

  return FastModularExponentiation(ConvertToInt(message), exponent, modulo)



def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def PowMod(b, e, m):
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
   


def Decrypt(ciphertext, p, q, exponent):
    modulo = p * q
    phi_n = (p - 1) * (q - 1)
    d = InvertModulo(exponent, phi_n)
    cipher2 = PowMod(ciphertext, d, modulo)
    return ConvertToStr(cipher2)
    





def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]



def small_big_prime_gen(modulo):
    prime_number = primes(1000000)
    
    for p in prime_number:
        q = modulo//p
        if p * q == modulo:
            return p,q
    return -1

def DecipherSmallPrime(ciphertext, modulo, exponent):
    
    if small_big_prime_gen(modulo) == -1:
        return "don't know"
    else:
        p,q = small_big_prime_gen(modulo)
        return Decrypt(ciphertext, p, q, exponent)
    


    