__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'




x = (input("Enter a number between 1 and 9999: "))
D = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
     '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven',
     '12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
     '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',
     '20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty',
     '70':'seventy','80':'eighty','90':'ninety','0':'hundred','000':'thousand'}
if len(x) == 1:
      if x in D.keys():
        print(D[x])
elif len(x) == 2:
    if x in D.keys():
        print(D[x])
    elif x[0] == '2':
        print(D['20']+' ' + D[x[1]])
    elif x[0] == '3':
        print(D['30']+' ' + D[x[1]])
    elif x[0] == '4':
        print(D['40']+' ' + D[(x)[1]])
    elif x[0] == '5':
        print(D['50']+' ' + D[x[1]])
    elif x[0] == '6':
        print(D['60']+' '+D[x[1]])
    elif x[0] == '7':
        print(D['70']+' '+D[x[1]])
    elif x[0] == '8':
        print(D['80']+' ' + D[x[1]])
    elif x[0] == '9':
        print(D['90']+' ' + D[x[1]])

elif len(x) == 3:
    if x[0] != '0' and x[1] == '0' and x[2] == '0':
         print(D[x[0]] + ' ' + D['0'])
    elif x[0] != '0' and x[1] != '0' and x[2] == '0':
            print(D[x[0]]+' hundred ' + D[x[1:]])
    elif x[0] != '0'and x[1] == '0' and x[2]!= 0:
        print(D[x[0]] + ' hundred ' + D[x[2]])
    else:
        if x[1:] in D.keys():
            print(D[x[0]] +' hundred '+D[x[1:]])
        elif x[1:] not in D.keys():
            if x[1] == '2':
                print(D[x[0]] +' hundred '+D['20']+ ' '+D[x[2]])
            elif x[1] == '3':
                print(D[x[0]] +' hundred '+D['30']+ ' '+D[x[2]])
            elif x[1] == '4':
                print(D[x[0]] +' hundred '+D['40']+ ' '+D[x[2]])
            elif x[1] == '5':
                print(D[x[0]] +' hundred '+D['50']+ ' '+D[x[2]])
            elif x[1] == '6':
                print(D[x[0]] +' hundred '+D['60']+ ' '+D[x[2]])
            elif x[1] == '7':
                print(D[x[0]] +' hundred '+D['70']+ ' '+D[x[2]])
            elif x[1] == '8':
                print(D[x[0]] +' hundred '+D['80']+ ' '+D[x[2]])
            elif x[1] == '9':
                print(D[x[0]] +' hundred '+D['90']+ ' '+D[x[2]])
elif len(x) == 4:
    if x[0]!= '0' and x[1] == '0' and x[2] == '0' and x[3]=='0':
        print(D[x[0]]+' thousand')
    elif x[0]!='0' and x[1]!= '0' and x[2]=='0' and x[3]=='0':
        print(D[x[0]]+' thousand '+D[x[1]]+' hundred')
    elif x[0]!='0' and x[1]!='0' and x[2]!= '0' and x[3] =='0':
        print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D[x[2:]])
    elif x[0]!='0'and x[1]!='0' and x[2] != '0' and x[3] != '0':
        if x[2:] in D.keys():
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D[x[2:]])
        elif x[2] == '2':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['20']+' '+D[x[3]])
        elif x[2]=='3':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['30']+' '+D[x[3]])
        elif x[2]=='4':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['40']+' '+D[x[3]])
        elif x[2]=='5':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['50']+' '+D[x[3]])
        elif x[2]=='6':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['60']+' '+D[x[3]])
        elif x[2]=='7':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['70']+' '+D[x[3]])
        elif x[2]=='8':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['80']+' '+D[x[3]])
        elif x[2]=='9':
            print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D['90']+' '+D[x[3]])
    elif x[0]!= '0' and x[1] == '0' and x[2]!='0' and x[3]!='0':
        if x[2:] in D.keys():
            print(D[x[0]]+' thousand '+D[x[2:]])
        elif x[2]=='2':
            print(D[x[0]]+' thousand '+D['20']+' '+D[x[3]])
        elif x[2]=='3':
            print(D[x[0]]+' thousand '+D['30']+' '+D[x[3]])
        elif x[2]=='4':
            print(D[x[0]]+' thousand '+D['40']+' '+D[x[3]])
        elif x[2]=='5':
            print(D[x[0]]+' thousand '+D['50']+' '+D[x[3]])
        elif x[2]=='6':
            print(D[x[0]]+' thousand '+D['60']+' '+D[x[3]])
        elif x[2]=='7':
            print(D[x[0]]+' thousand '+D['70']+' '+D[x[3]])
        elif x[2]=='8':
            print(D[x[0]]+' thousand '+D['80']+' '+D[x[3]])
        elif x[2]=='9':
            print(D[x[0]]+' thousand '+D['90']+' '+D[x[3]])
    elif x[0]!= '0' and x[1] == '0' and x[2]=='0' and x[3]!='0':
        print(D[x[0]]+' thousand '+D[x[3]])
    elif x[0]!= '0' and x[1] != '0' and x[2]=='0' and x[3]!='0':
        print(D[x[0]]+' thousand '+D[x[1]]+' hundred '+D[x[3]])

