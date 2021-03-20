__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# Write a function named calculate_expenses that receives a filename as argument. The file contains the information
# about a person's expenses on items. Your function should return a list of tuples sorted based on the name of the items.
#  Each tuple consists of the name of the item and total expense of that item as shown below:

# milk,2.35
# bread , 1.95
#  chips ,    2.54
# milk  ,    2.38
# milk,2.31
# bread,    1.90


#Notice that each line of the file only includes an item and the purchase price of that item separated by a comma.
# There may be spaces before or after the item or the price. Then your function should read the file and return a list
# of tuples such as:

# [('bread', '$3.85'), ('chips', '$2.54'), ('milk', '$7.04')]

# Notes:

#  Tuples are sorted based on the item names i.e. bread comes before chips which comes before milk.
#  The total expenses are strings which start with a $ and they have two digits of accuracy after the decimal point.
#  Hint: Use "${:.2f}" to properly create and format strings for the total expenses.



def calculate_expenses(file):

    file = open(file,'r')
    file = file.readlines()
    LL = []

    for line in file:
        line = line.rstrip().split(',')           # Remove newLine character and split by comma.
        line = [x.replace(' ','') for x in line]  # Remove extra space
        LL += [line]

    LN = []

    for i in LL:                                  # Collect all the items name with duplicates
        LN += [i[0]]

    D = {}

    for name in LN:

        summ = 0
        if LN.count(name) > 1:                   # Check if items occur more than one
            for item in LL:
                if item[0] == name:
                    summ += float(item[1])       # Then sum all items cost
            D[name] = summ
        else:
            for item in LL:
                if item[0] == name:
                    D[name] = float(item[1])

    from collections import OrderedDict
    from operator import itemgetter
    D = OrderedDict(sorted(D.items(), key=itemgetter(0)))   # Sort by item names

    LLL = []

    for k, v in D.items():
        LLL += [(k,'${0:1.2f}'.format(float(v)))]          # follows question specification
    return LLL
#print(calculate_expenses('a2.txt'))