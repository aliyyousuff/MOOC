__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'

# Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a
# crossword puzzle) and a string (word) as input arguments. This function searches the rows of the 2d
# list to find a match for the word. If a match is found, this functions returns a list containing row
# index and column index of the start of the match, otherwise it returns the value None (no quotations).

# For example if the function is called as shown below:

#     crosswords = [['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]

#     word= 'cat'
# then your function should return [2,1]
# Notice that the 2d input list represents a 2d crossword and the starting index of the horizontal word
# 'cat' is [2,1]



def find_word_horizontal(crosswords,word):
    wo = [i for i in word]
    L = []

    for ir in range(len(crosswords)):
        for ic in range((len(crosswords[0])-len(word))+1):
            w = crosswords[ir][ic:len(word)+ic]              # Slicing word following words length
            if wo == w:
                L = [ir,ic]                                  # Saving row and column index
            else:
                pass
    if not L:
        return None
    else:
        return L

c1=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
w1 = 'cat'
c2 = [['a', 'b'], ['c', 'd']]
w2 = 'b'
c3 = [['a', 'b'], ['c', 'd']]
w3 = 'ab'
c5 = [['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
w5 = 'cat'
print(find_word_horizontal(c1,w1))



