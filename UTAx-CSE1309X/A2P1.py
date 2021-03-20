__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'

# Assignment 2 Part 02:
# Write a function named find_mismatch that accepts two strings as input arguments and returns:
# 0 if the two strings match exactly.
# 1 if the two strings have the same length and mismatch in only one character.
# 2 if the two strings do not have the same length or mismatch in two or more characters.

# Capital letters are considered the same as lower case letters. Here are some examples:
#
#  First string	Second String	Function return
#  Python	         Java	               2
#  Hello There	    helloothere	           1
#  sin	            sink	                           2 (note not the same length)
#  dog	            Dog	                   0

def find_mismatch(str1,str2):
    count = 0
    for chr1,chr2 in zip(str1.lower(),str2.lower()):
             if chr1!= chr2:
                 count +=1
    if str1.lower() == str2.lower():
        return 0
    elif len(str1) == len(str2) and count == 1:
        return 1

    else:
       return 2

#print(find_mismatch ('Ruby', 'Java'))