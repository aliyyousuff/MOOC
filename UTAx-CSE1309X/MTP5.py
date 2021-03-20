#Write a function named items_price that accepts two lists as parameters. The first list contains the quantities of n
# different items, the second list contains the prices that correspond to those n items respectively. Now, calculate
# the total amount of money required to purchase those items.
# a = [2, 3, 5, 7, 9]
# This list (list a) gives you the quantity of each item.
# b = [5, 8, 4, 1, 11]

def items_price(a,b):
    money = 0
    for chr1,chr2 in zip(a,b):
        money += chr1*chr2
    return money

