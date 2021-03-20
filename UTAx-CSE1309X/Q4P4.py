__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'


# Write a function named test_for_anagrams that receives two strings as parameters,
# both of which consist of alphabetic characters and returns True if the two strings
# are anagrams, False otherwise. Two strings are anagrams if one string can be constructed
#  by rearranging the characters in the other string using all the characters in the
# original string exactly once. For example, the strings "Orchestra" and "Carthorse"
# are anagrams because each one can be constructed by rearranging the characters in the
# other one using all the characters in one of them exactly once.
# Note that capitalization does not matter here i.e. a lower case character can be
# considered the same as an upper case character


def test_for_anagrams(s1,s2):
    s1,s2 = s1.lower(),s2.lower()
    D,D2 = {},{}
    for char in s1:
        D[char] = s1.count(char)
    for char in s2:
        D2[char] = s2.count(char)
    mis_match = 0
    for k,v in D.items():
        try:
           if D[k] != D2[k]:
              mis_match += 1
        except KeyError:
            return False

    if not mis_match and len(D) == len(D2):
        return True
    else:
        return False


print(test_for_anagrams('hello','hallo'))