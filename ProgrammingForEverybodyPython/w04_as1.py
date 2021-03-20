 # Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
 # Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of 
 # time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a 
 # value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to 
 # read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want 
 # to - you can assume the user types numbers properly.
 


def computepay(hours,rate):
    if hours < 0 or rate < 0:
        print 'Please enter valid number'
    elif hours > 40:                                  # More than 40.
        extra_hours = hours - 40                      #Calculate extra hours of work.

        return (40 * rate) + (extra_hours * rate*1.5)  # Following question we have to multiply extra hour by 1.5.
    else:
        return hours * rate
try:                                     # Here we use TRY function to see how our function works.
    hrs = raw_input("Enter hours: ")
    hours = float(hrs)
    rt = raw_input("Enter rate: ")
    rate = float(rt)
    total_pay = computepay(hours,rate)
    print total_pay
except:
    print "Enter a valid numerals"
  
  # If this code helps you,give a <fb.com/cloudboyc> thanks. Your feedback would be appreciated.
