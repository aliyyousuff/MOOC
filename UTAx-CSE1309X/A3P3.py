__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'

# Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of
# characters (like a crossword puzzle) and a string (word) as input arguments. This function
#  searches the rows and columns of the 2d list to find a match for the word. If a match
# is found, this functions capitalizes the matched characters in 2-dimensional list and
# returns the list. If no match is found, this function simply returns the origianl
# 2-dimensional list with no modification.




def find_word_horizontal(crosswords,word):
    wo = [i for i in word]
    L = []

    for ir in range(len(crosswords)):
        for ic in range((len(crosswords[0])-len(word))+1):
            w = crosswords[ir][ic:len(word)+ic]
            if wo == w:
                L = [ir,ic]
            else:
                pass
    if not L:
        return None
    else:
        return L


def find_word_vertical(crosswords, word):

    L = []
    for i in range(len(crosswords[0])):
       W = ''
       for ii in crosswords:
           W += ii[i]
       for k in range(len(W)-len(word)+1):
           if W[k:len(word)+k] == word:
               L += [[k,i]]
    if not L:
        return None
    else:
       return L[0]

def capitalize_word_in_crossword(crosswords,word):

    L1 = find_word_horizontal(crosswords,word)
    L2 = find_word_vertical(crosswords, word)

    if L1 is not None and L2 is not None:
        if len(word) == 1:
            for element in (crosswords[L1[0]][L1[1]:]):
                crosswords[L1[0]][crosswords[L1[0]].index(element)] = element.capitalize()
            return crosswords
        else:
            for element in range(L1[1],(len(crosswords[L1[0]][L1[1]:]))+1):
                crosswords[L1[0]][element] = crosswords[L1[0]][element].capitalize()
            return crosswords
    elif L1 is None and L2 is not None:
       #
       for element2 in range(L2[0], len(crosswords)):
            crosswords[element2][L2[1]] = crosswords[element2][L2[1]].capitalize()
       return crosswords
    elif L1 is not None and L2 is None:
        if len(word) == 1:
            for element in (crosswords[L1[0]][L1[1]:]):
                crosswords[L1[0]][crosswords[L1[0]].index(element)] = element.capitalize()
            return crosswords
        else:
            for element in range(L1[1],(len(crosswords[L1[0]][L1[1]:]))):
                crosswords[L1[0]][element] = crosswords[L1[0]][element].capitalize()
            return crosswords
    else:
        return crosswords

c1=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
w1 = 'cat'
c2 = [['a', 'b'], ['c', 'd']]
w2 = 'b'
c3 = [['a', 'b'], ['c', 'd']]
w3 = 'ab'
c4 = [['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
w4 = 'cat'
c5 = [['s', 'd', 'o', 'g'], ['x', 'u', 'c', 'm'], ['a', 'x', 'a', 't'], ['t', 'e', 't', 'k']]
w5 = 'cat'

T = [(c1,w1),(c2,w2),(c3,w3),(c4,w4),(c5,w5)]
for i in T:
    print(capitalize_word_in_crossword(i[0],i[1]))





