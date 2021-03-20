__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf,aliyyousuf@gmail.com'

# Write a function named count_consonants that receives a string as parameter and returns the total count of the
# consonants in the string. Consonants are all the characters in the english alphabet except for 'a', 'e', 'i',
# 'o', 'u'. If the same consonant repeats multiple times you should count all of them. Note that capitalization
# and punctuation does not matter here i.e. a lower case character should be considered the same as an upper case
#  character.


def count_consonants(some_string):

     some_string = some_string.lower()
     some_string = some_string.replace(' ','')
     vowel = 'aeiou'
     for v in vowel:
         some_string = some_string.replace(v,'')

     return len(some_string)

print(count_consonants('Hercules was a hero'))