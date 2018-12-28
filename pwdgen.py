#!python3
#
# A training program to generate passwords of a given lenght from alphanumeric and
# special characters.
#
# The menu could be extended to fit various common restrictions on acceptable passwords.

from random import choices
from string import punctuation, ascii_letters, digits
import tkinter 

root = tkinter.Tk()
root.withdraw()

n = int(input("How may characters should the password consist of?\n"))
if n == 0:
    n = 12
p = ""
q = (input("May it contain punctuation and special characters? (y/n)\n").lower())
if q == "y":
    p = punctuation
elif q != "n":
    print("I guess not... ")

pwd = ("".join(choices(list(ascii_letters+digits+p),k = n)))

root.clipboard_clear()
root.clipboard_append(pwd)

print("Your new Password > {0} < has been copied to clipboard".format(pwd))

root.destroy()

input("\nPress 'Return' to exit")
