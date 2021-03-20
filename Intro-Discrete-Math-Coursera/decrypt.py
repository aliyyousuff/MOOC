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


def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod


def Decrypt(ciphertext, p, q, exponent):
    modulo = p * q
    phi_n = (p - 1) * (q - 1)
    d = InvertModulo(exponent, phi_n)
    cipher2 = PowMod(ciphertext, d, modulo)
    return ConvertToStr(cipher2)
    
