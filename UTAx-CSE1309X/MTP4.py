def list_of_primes(xx):

    return ([x for x in range(2,xx) if not [t for t in range(2,x) if not x%t]])

print(list_of_primes(1000))
