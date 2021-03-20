__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

# Write a program that asks the user for a positive number
# 'n' as input. Assume that the user enters a number greater
# than or equal to 3 and print a triangle as described below.
# For example if the user enters 6 then the output should be:
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *


n = int(input("Enter a number: "))
for i in range(1,n+1):
        print(i*'*')
while n > 1:
        n = n-1
        print(n*'*')


