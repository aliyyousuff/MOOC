__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf,aliyyousuf@gmail.com'

# Write a function named find_longest_word that receives a string as parameter
# and returns the longest word in the string. Assume that the input to this
# function is a string of words consisting of alphabetic characters that are
# separated by space(s). In case of a tie between some words return the last one
# that occurs.



def find_longest_word(some_string):
   from collections import OrderedDict  # OrderedDict saves key ordered following entering
   list_words =some_string.split()
   D  = OrderedDict()
   for i in list_words:
       D[i] = len(i)
   val = list(D.values())
   max_val = max(val)
   LL = []
   for k,v in D.items():
       if D[k] == v:
           LL += [k]
   return(LL[-1])        # If multiple words have the same max length, return the last one.


print(find_longest_word('brahman the mysterious of the univERsity'))