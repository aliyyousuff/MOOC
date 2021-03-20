__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


# Complete the following program such that it calculates and prints the average
# of the elements of the given list.

sample_list = [2,10,3,5]
summ = 0
for x in sample_list:
    summ += x

print(summ/len(sample_list))
