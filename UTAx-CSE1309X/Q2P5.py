__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

total_secs = int(input("How many seconds, in total?  " ))

days = total_secs // 86400
secs_days = total_secs % 86400
#calculate the remainder into hours
hours = secs_days // 3600
secs_hours = secs_days % 3600
#calculate the remainder into minutes
minutes =  secs_hours // 60
secs_minutes = secs_hours % 60
#calculate the remainder into seconds
seconds = secs_minutes
print( str(days) + ' days ' + str(hours)+ ' hours ' + str(minutes) + ' minutes ' + str(seconds) + ' seconds')


