__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


D = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}







def reverse_dictionary(D):

    D3 = {}
    for k,v in D.items():
         D3[k.lower()] = [x.lower() for x in v]

    D2= {}
    for k,v in D3.items():
        if len(v) > 1:
            for e in v:
                if e not in D2.keys():
                    D2[e] = [k]
                else:
                    D2[e] += [k]
        else:
            if v[0] not in D2.keys():
                D2[v[0]] = [k]
            else:
                D2[v[0]] += [k]

    D4 = {}
    for k,v in D2.items():
        D4[k] = sorted(v)
    return D4



D2 = {'astute': ['Smart', 'clever', 'talented'], 'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'talented': ['smart', 'keen', 'Bright'], 'smart': ['clever', 'bright', 'talented']}


print(reverse_dictionary(D2))

