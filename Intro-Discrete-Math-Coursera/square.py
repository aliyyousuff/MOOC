# Given an n×m grid (where n,m are integers), you would like to tile it with the minimal number of same size squares. Clearly, 
# it can always be tiled with nm squares of size 1×1, but it is not always optimal. For example, a 6x10 grid can be tiled by 15 s
# quares of size 2×2:

def squares(n,m):
    area = m * n
    while n> 0 and m > 0:
        if n >= m:
            n = n% m
        else:
            m = m % n
    return int(area / (max(m,n))**2)
