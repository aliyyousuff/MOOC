__author__ = 'Mohammad Yousuf Ali,fb.com/aliyyousuf,aliyyousuf@gmail.com'

# Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence
# (string) and the second argument is a list of words (correct_spells). Your function should check each
# word in the input string against all the words in the correct_spells list and return a string such that:

# If a word in the original sentence matches exactly with a word in the correct_spells then the word is not
# modified and it should be directly copied to the output string.
# if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or
# deleting a single character, then that word should be replaced by the correct word in the correct_spelled
#  list.
# If neither of the two previous conditions is true, then the word in the original string should not be
# modified and should be directly copied to the output string.

def exact_match(st1,st2):

    if len(st1) == len(st2) and st1.lower() == st2.lower():
        return True
    else:
        return False


def del_by_1(st1,st2):

    st1 = st1.lower()
    try:
        assert len(st1)-len(st2) == 1
    except AssertionError:
        return False
    all_possible = [st1[:i]+st1[i+1:] for i in range(len(st1))]
    if st2.lower() in all_possible:
        return True
    else:
        return False



def insert_by_one(st1,st2):

    import string
    alphabet =string.ascii_lowercase
    st1 = st1.lower()
    st2 = st2.lower()

    try:
        assert len(st1) - len(st2) == -1
    except AssertionError:
        return  False

    r = False
    for index in range(len(st1)):
            for char in alphabet:
                    if st1[0:index] + char + st1[index:len(st1)] == st2:
                            r =  True
                            break

    for char in alphabet:
        if st1+ char == st2:
            r = True
            break

    return r

def replace_by_one(st1,st2):

    st1 = st1.lower()
    st2 = st2.lower()
    try:
       assert len(st1) == len(st2)  and st1 != st2
    except AssertionError:
        return False

    count = 0
    index = []
    for chr1,chr2 in zip(st1,st2):
        if chr1 != chr2:
            count += 1
            index += [st1.index(chr1)]
    if count == 1:
        return True
    else:
        False


def spelling_corrector(st,L):

    import re
    st = st.lower()
    L = [i.lower() for i in L]
    st_L = st.split()

    for char1 in st_L:
            for char2 in L:
                if exact_match(char1,char2):
                   st = st.replace(char1,char2)
                elif char1 in L:
                    st.replace(char1,char2)
                    break
                elif del_by_1(char1,char2):
                    st = st.replace(char1,char2)
                    break
                elif replace_by_one(char1,char2):
                    st = st.replace(char1,char2)
                    break
                elif insert_by_one(char1,char2):
                    st = st.replace(char1,char2)
                    break
    st = st.rstrip()
    return re.sub(r'\s{2,}', ' ', st)

s = 'programing   is fan and eesy'
l = ['programming', 'this', 'fun', 'easy', 'book']
L = (spelling_corrector(s,l))
