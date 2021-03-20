__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'



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

def print_grades(file_name):

    import collections
    DD = create_grades_dict(file_name)
    DD = collections.OrderedDict(sorted(DD.items()))    # sort the dictionary

    print('{0:''^10s} | {1:''^16s} | {2:''^6s} | {3:''^6s} | {4:''^6s} | {5:''^6s} | {6:''^6s} |'.format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.'))
    for k,v in DD.items():
        print('{0:''<10s} | {1:''<16s} | {2:''>6d} | {3:''>6d} | {4:''>6d} | {5:''>6d} | {6:''>6.2f} |'\
        .format(k,v[0],v[1],v[2],v[3],v[4],v[5]))
print(print_grades('a.txt'))