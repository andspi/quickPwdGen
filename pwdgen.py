#!python3
#
# A training program to generate passowrds of a given lenght from alphanumeric and
# special characters.
#
# Complete.
#
# Might be modified to directly return the results to the windows clipboard!
# The menu could be extended to fit various common restrictions on acceptable passwords.
# 

import random
import string

n = int(input("How may characters should the password consist of?\n"))
if n == 0:
    n = 12
p = ""
q = (input("May it contain punctuation and special characters? (y/n)\n").lower())
if q == "y":
    p = string.punctuation

print("{1}\n{0} characters\n{1}\nYour new PWD:{1}".format(n,"\n++++++++++++++"))

print("".join(random.choices(list(string.ascii_letters+string.digits+p),k = n)))

input("\nPress 'Return' to exit")
    
