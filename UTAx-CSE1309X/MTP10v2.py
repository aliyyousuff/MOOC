__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'




#x = (input("Enter a number between 1 and 9999: "))
D = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
     '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven',
     '12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
     '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',
     '20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty',
     '70':'seventy','80':'eighty','90':'ninety','00':'hundred','000':'thousand'}

keys = D.keys()
def two_number(x):
    D = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
     '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven',
     '12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
     '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',
     '20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty',
     '70':'seventy','80':'eighty','90':'ninety','00':'hundred','000':'thousand'}
    if x in D.keys():
        return D[x]
    elif x[0] == '2':
        return D['20']+' ' + D[x[1]]
    elif x[0] == '3':
        return D['30']+' ' + D[x[1]]
    elif x[0] == '4':
        return D['40']+' ' + D[(x)[1]]
    elif x[0] == '5':
        return D['50']+' ' + D[x[1]]
    elif x[0] == '6':
        return D['60']+' '+D[x[1]]
    elif x[0] == '7':
        return D['70']+' '+D[x[1]]
    elif x[0] == '8':
        return D['80']+' ' + D[x[1]]
    elif x[0] == '9':
        return D['90']+' ' + D[x[1]]

def three_number(x):
    D = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
     '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven',
     '12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
     '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',
     '20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty',
     '70':'seventy','80':'eighty','90':'ninety','00':'hundred','000':'thousand'}
    if x[1:] == '00':
        return D[x[0]]+ ' ' + D[x[1:]]
    elif x[:2] != '00' and x[2] == '0':
        return two_number(x[:2]) + ' '+  D['00']
    elif x[0] != '0' and x[1]=='0'and x[2] != '0':
        return D[x[0]] + ' hundred ' + D[x[2]]
    elif x[0] != '0' and x[1] != '0' and x[2] != '0':
        return D[x[0]] + ' hundred ' + two_number(x[1:])
def four_number(x):
    D = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
     '7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven',
     '12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
     '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',
     '20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty',
     '70':'seventy','80':'eighty','90':'ninety','00':'hundred','000':'thousand'}
    if x[0] != '0' and x[1:] == '000':
        return D[x[0]] +' thousand'
    elif x[0] != '0' and x[1] != '0' and x[2:] == '00':
        return two_number(x[0]) + ' thousand ' + two_number(x[1]) + ' hundred'
    elif x[0] != '0' and x[1] != '0' and x[2] != '0' and x[3] == '0':
        return D[x[0]]+' thousand '+D[x[1]]+' hundred '+two_number(x[2:])
    elif x[0] != '0' and x[1] != '0' and x[2] != '0' and x[3] != '0':
        return D[x[0]]+' thousand '+D[x[1]]+' hundred '+two_number(x[2:])
    elif x[0] != '0' and x[1] == '0' and x[2] != '0' and x[3] != '0':
        return D[x[0]]+' thousand ' +two_number(x[2:]) +' '
    elif x[0] != '0' and x[1] == '0' and x[2] == '0' and x[3] != '0':
        return D[x[0]]+' thousand ' +two_number(x[3])
def final(x):

   if len(x) == 1:
      return(D[x])
   elif len(x) ==2:
      return (two_number(x))
   elif len(x) ==3:
      return (three_number(x))
   elif len(x) == 4:
      return (four_number(x))
   else:
    return ('Enter a valid number')
test = ['1','7','100','111','501','100','111','999','1000','1100','1110','1001','1011','1111','1510','3421','7000','1008','9999']
print("Testing case,please ignore the space after :")
for x in test:
   print("When testing case is " + x + " my code returns: "+final(x))
#print(final(x))