__author__ = "aliyyousuf@gmail.com"


def count_vowels(word):
    '''Write a function count_vowels(word) that takes the string word as input and returns the number of occurrences of lowercase vowels (i.e. the lowercase letters "aeiou") in word. Hint: Python has a built-in string method that can count the number of occurrences of a letter in a string.'''

    vowel = "aeiou"
    count = 0

    for v in vowel:
        for w in word:
            if v == w:
                count += 1
            else:
                pass

    return count

#print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

def demystify(word):
    '''Write a function demystify(l1_string) that takes a string composed of the characters "l" and "1" and returns the string formed by replacing each instance of "l" by "a" and each instance of "1" by "b".'''

    word = word.replace("l","a")
    word = word.replace("1","b")
    return word
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))