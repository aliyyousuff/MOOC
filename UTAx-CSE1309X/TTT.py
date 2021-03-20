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

    if L1 is not None:
        for element in (crosswords[L1[0]][L1[1]:]):
            crosswords[L1[0]][crosswords[L1[0]].index(element)] = element.capitalize()
    else:
        for element2 in range(L2[0], (len(crosswords[L2[1]][L2[1]:]))):
            crosswords[element2][L2[1]] = crosswords[element2][L2[1]].capitalize()
    return crosswords

c1=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
w1 = 'cat'
c2 = [['a', 'b'], ['c', 'd']]
w2 = 'b'
c3 = [['a', 'b'], ['c', 'd']]
w3 = 'ab'
c5 = [['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
w5 = 'cat'

print(capitalize_word_in_crossword(c1,w1))





