def find_integer_with_most_divisors(L):
    import collections
    D = collections.OrderedDict()

    LL2 = []
    for i in L:
        LL = []
        for ii in range(1,i+1):
            for iii in range(1,i+1):
                if ii * iii == i:
                    LL += [ii]
        D[i] = len(LL)
    max_val = max(D.values())
    for k, v in D.items():
        if v == max_val:
            LL2 += [k]
    return LL2[0]

k = [12, 24, 6, 18]
print(find_integer_with_most_divisors(k))