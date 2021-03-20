
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

def remaining_loan(P,AIR,D,NP):
    r1 = AIR/100
    r = r1/12
    n = D * 12
    if r == 0:
        mp = P * (1 - P/NP)
    else:
        p1 = (((1+r) ** n) - ((1 + r) ** NP))
        p2 = (((1+r)**n)-1)
        mp = P * (p1/p2)
    return mp
#print(remaining_loan(1000.0,4.5,5,12))
for y in range(1,6):
    rm = remaining_loan(1000.0,4.5,5,y*12)
    py = y*12
    print(('YEAR: ' + str(y)+ ' BALANCE: ' + str(int(rm)) + ' TOTAL PAYMENT '+str(int(py*monthly_payment(1000.0,4.5,5)))))


