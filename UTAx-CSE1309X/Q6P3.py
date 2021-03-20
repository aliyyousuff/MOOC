__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

# Write a function named calculate_grades that receives a file name. The file contains
# names of students and their grades for 4 quizzes and returns a tuple as specified
# below. Each line of the file will have the following format:

# name,quiz1_score,quiz2_score,quiz3_score,quiz4_score

# For example if the contents of the file are:

#    john,89,94,81,97
#    eva,40,45,65,90
#    joseph,0,0,54,99
#    tim,73,74,89,91

# The name and grades are separated by commas. Your function should return the names of
#  the student and their quiz averages as a tuple of tuples as shown below:

# (('eva', 60.0), ('john', 90.25), ('joseph', 38.25), ('tim', 81.75))

# The tuples should be sorted in ascending order by the student's name.



def calculate_grades(file_name):

    file  = open(file_name,'r')
    file = file.readlines()
    LL = []

    for i in file:
       LL += [i.strip().split(',')]

    t = []

    for i in LL:
       sum = 0
       count =0
       for ii in i[1:]:
           count += 1
           sum += int(ii)
       t += [(i[0],sum/count)]
    t.sort(key = lambda tup: tup[0])

    return tuple(t)

# print(calculate_grades('aa.txt'))
