__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'


# Write a function named create_grades_dict that accepts a string as the name of a file. Assuming that the file is a text
# file which includes name and grades of students, your function should read the file and return a dictionary with the
# exact format as shown below: The format of the input file is:

# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..

# An example of the input file is shown below. Sample Input Output Assuming that the input file "student_grades.txt"
# contains the following text:
# 1000123456, Rubble, Test_3,  80, Test_4 , 80
# 1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88


# Your function should read the input file, calculate the average test grade for each student and return a dictionary
# with the following format:
# {'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}
# For example in the case of sample input file shown above, your function should return the following dictionary:
# {'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}


def create_grades_dict(file_name):

    file = open(file_name,'r')                    # Reading the file elements

    file = file.readlines()
    D = {}

    for line in file:

        line = line.rstrip().split(',')                    # split string from .readlines() method by comma.
        line = [x.replace(' ','') for x in line]           # remove extra space from each element from list's items
        D[line[0]] = [line[1]]                             # Select student's ID as  the key of dict

        for t in ['Test_1', 'Test_2', 'Test_3', 'Test_4']:   # Check if tests are in file's data
            if t  in line:
                D[line[0]] += [int(line[1+line.index(t)])]   # If it is then select its value
            else:
                D[line[0]] +=[0]                                  # If it is not then select the value of that test is zero
        D[line[0]] += [sum(D[line[0]][1:])/len(D[line[0]][1:])]   # Calculate average of Total test's value
    return D

