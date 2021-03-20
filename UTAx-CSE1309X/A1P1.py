__author__ = 'Mohammad Yousuf Ali'
def monthly_payment(P,A,D):
    r1 = A/100
    r = r1/12
    n = D * 12
    if r == 0:
        mp = P/n
    else:
        mp = P * (r*(1+r)**n)/((1+r)**n - 1)
    return mp


