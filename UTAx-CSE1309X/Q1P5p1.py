__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


# Write a program that asks the user for a positive integer between 1 and 7 (Assume that the user
# may enter any number from 1 to 7 both inclusive) and prints the day of week corresponding to
# that number in all capital letters. Assume that the day of the week starts from MONDAY.


weeks = {1:'MONDAY', 2:"TUESDAY", 3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY',7:'SUNDAY'}

day_number = int(input("Enter a number between 1 and 7: "))

if day_number > 0 and day_number <=7:
    print(weeks[day_number])
else:
    print("Please enter a number between 1 and 7")