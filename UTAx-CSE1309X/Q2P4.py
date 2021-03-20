__author__ = ' Mohammad Yousuf Ali, aliyyousuf@gmail.com'



h = int(input('Enter total hour: '))
if h < 0 or h > 168:
    print('INVALID')
elif h <= 40:
    print('YOU MADE ' + str((h * 8)) + ' DOLLARS THIS WEEK')
elif h > 40 and h < 50:
    print(('YOU MADE ' + str((40*8) + (h - 40)*9)) + ' DOLLARS THIS WEEK')
elif h >= 50:
    print('YOU MADE ' + str(((40*8)+(h - 40)*10)) + ' DOLLARS THIS WEEK')



