def gcd(a,b):
    assert a>= a and b >= 0 and a + b > 0
    
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a,b)


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def diophantine(a,b,c):
    
    assert c % gcd(a, b) == 0
    (d, u, v) = egcd(a,b)
    
    x = u * (c // gcd(a,b))
    y = v * (c//gcd(a,b))
    
    
    return (x,y)

def divide(a,b,n):
    assert n > 1 and a > 0 and gcd(a,n) == 1
    t,s = diophantine(n,a,1)
    
    for i in range(n):
        if b * s % n == i % n:
            return i
        

    



