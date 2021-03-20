__author__ = 'Mohammad Yousuf Ali,aliyyousuf@gmail.com'


def MY_2D_LIST(n):
    r1, r2 = [1], [1, 1]
    degree = 1
    R = []
    while degree <= n:
        R += [r1]
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
        degree += 1
    return R
