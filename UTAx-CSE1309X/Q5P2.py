__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, aliyyousuf@gmail.com'


# Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter
# and returns a dictionary whose values would be the maximum value of each row and whose keys
# would be the appropriate strings as specified below.

def row_maximums(multi_dm_list):

    D = {}

    for i in range(len(multi_dm_list)):
        D['row '+str(i)+' max'] = max(multi_dm_list[i])

    return D


L = [[5, 0, 0, 0, 13],[0, 12, 0, 0],[20, 0, 11, 0],[6, 0, 0, 8]]

print(row_maximums(L))