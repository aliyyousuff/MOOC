__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'


# Write a function named my_encryption that accepts a string (a message which will only
# consist of the characters from the character set) as function parameter and encrypts that
# message using the secret_key and returns it. For example if input to this function
# (the message that you want to send) is:
#  "Lets meet at the usual place at 9 am"

#  Then your function should should return the encrypted message:
#      "oABjMWAABMDBMB2AMvjvDPMYPD1AMDBMGMDW"
#   Note that capitalization does matter here!



def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    D = {}
    encrypt_string = ''
    for char1,char2 in zip(character_set,secret_key):
        D[char1] = char2

    for char in some_string:
        encrypt_string += D[char]
    return encrypt_string

s = "Lets meet at the usual place at 9 am"

print(my_encryption(s))