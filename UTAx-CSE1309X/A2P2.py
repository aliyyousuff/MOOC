__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'


# Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:
# 0 if the two strings match exactly.
# 1 if the first string can become the same as the second string by inserting or deleting a single character. Notice that
# inserting and deleting a character is not the same as replacing a character.
# 2 otherwise
# Capital letters are considered the same as lower case letters. Here are some examples:


# First string	Second String	Function return
#    Python	        Java	           2
#     book	        boot	           2
#     sin	        sink	           1 (Inserting a single character at the end)
#     dog	         Dog	           0
#     poke	         spoke	           1 (Inserting a single character at the start)
#     poker	         poke	           1 (Deleting a single character from the end)
#     programing	 programming	   1 (Inserting a single character)

def single_insert_or_delete(s1,s2):
    s1,s2 = s1.lower(),s2.lower()
    count = 0
    for chr1,chr2 in zip(s1,s2):
             if chr1!= chr2:
                 count +=1
    if s1 == s2:
        return 0
    elif len(s1)-len(s2) == 1 or len(s1)-len(s2)==-1:
        return 1
    else:
        return 2
#print(single_insert_or_delete('poke','spoke'))