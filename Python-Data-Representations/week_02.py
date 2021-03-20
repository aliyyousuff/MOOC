__author__ = "aliyyousuf@gmail.com"

def strange_sum(numbers):
    summ = 0
    for n in numbers:
        if n % 3 != 0:
            summ += n
        else:
            pass
    return summ
print(strange_sum(list(range(123)) + list(range(77))))