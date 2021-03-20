import re
import operator


file = open('w2_dat.txt','r')
numbers = list()
s = []

for line in file:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if len(num) <= 0:
        pass
    else:
        for i in num:
           numbers.append(int(i))
    #numbers = [x for sublist in numbers for x in sublist]
print(sum(numbers))