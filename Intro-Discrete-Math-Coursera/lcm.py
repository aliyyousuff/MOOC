# lcm function returns the least common multiple of
# two given integers using Euclidean Algorithm to calculate
# Greatest Common Divisor.


def lcm(a,b):
    m,n = a,b
    assert a > 0 and b > 0
    while a>0 and b > 0:
        if a>=b:
            a = a%b
        else:
            b = b %a
    return  m*n / max(a,b)

print(lcm(35,70))
