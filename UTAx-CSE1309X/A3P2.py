__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# Write a function named find_word_vertical that accepts a 2-dimensional list of characters (like
# a crossword puzzle) and a string (word) as input arguments. This function searches the columnss of
# the 2d list to find a match for the word. If a match is found, this functions returns a list
# containing row index and column index of the start of the match, otherwise it returns the value
# None (no quotations).

def find_word_vertical(crosswords, words):

    L = []
    for i in range(len(crosswords[0])):
       W = ''
       for ii in crosswords:
           W += ii[i]
       for k in range(len(W)-len(words)+1):
           if W[k:len(words)+k] == words:
               L += [[k,i]]
    if not L:
        return None
    else:
       return L[0]
c1=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
w1 = 'cat'
c2 = [['a', 'b'], ['c', 'd']]
w2 = 'b'
c3 = [['a', 'b'], ['c', 'd']]
w3 = 'ab'
c5 = [['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
w5 = 'cat'
c4 = [['s', 'd', 'o', 'g'], ['x', 'u', 'c', 'm'], ['a', 'x', 'a', 't'], ['t', 'e', 't', 'k']]
w4 = 'cat'
print(find_word_vertical(c4,w4))


