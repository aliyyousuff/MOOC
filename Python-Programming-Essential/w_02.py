__author__ = "aliyousuuf@gmail.com"

# Q.07: Collatz Conjecture

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3  + 1
#print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))
