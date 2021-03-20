

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

