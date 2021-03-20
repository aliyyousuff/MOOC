
def my_final_grade_calculation(filename):


    file = open(filename,'r')
    file = file.readlines()
    L = []
    for i in file:
        L+= [i.rstrip().split(',')]
    L2 = []
    for i in L:
        L3 = []
        L4 = []
        for k in i:
            L3.extend([k.replace(' ','')])
        for j in L3[1:]:
            L4.extend([int(j)])
        L4.insert(0,L3[0])
        L2 += [L4]
    #print(L2)
    D = {}
    for i in L2:
        L1 = sorted(i[1:7])
        LQ = sum(L1[2:])/len(L1[2:])
        LQ = (25/100)* LQ
        LA = sorted(i[7:11])
        LA = sum(LA[1:])/len(LA[1:])
        LA = (25/100)*LA
        LMF = i[-2]*0.25 + i[-1]*0.25
        if (LQ+LA+LMF) >= 60:
            D[i[0].lower()] = 'pass'
        else:
            D[i[0].lower()] = 'fail'
    return D

#print(my_final_grade_calculation('f.txt'))







