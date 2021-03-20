# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a 
# string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types 
# numbers properly.

hrs = raw_input("Enter Hours:")
h = float(hrs)
if h > 40:
    extra_time = h - 40
    pay_per_hours = raw_input('Enter hourly payment: ')
    hourly_pay = float(pay_per_hours)
    total_pay = 40 * hourly_pay + (extra_time * hourly_pay) * 1.5
print total_pay
