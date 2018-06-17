#!python3
#
# A training program to generate passowrds of a given lenght from alphanumeric and special characters.
#
# Why is the clipboard data only available after I exit the program?
# Why does this not run in Atom - is there no loading of moduls?
#
# The menu could be extended to fit various common restrictions on acceptable passwords.
#
#

from random import choices
from string import punctuation, ascii_letters, digits
from tkinter import Tk

r = Tk()
r.withdraw()

n = input("How may characters should the password consist of?\n")
if isinstance(n,(int,float)):
    n = int(n)
else:
    n = 12
    print("Not a valid value! Set to {0}\n".format(n))

q = (input("May it contain punctuation and special characters? (y/n)\n").lower())
if q == "y":
    p = punctuation
else:
    p = ""

c = "".join(choices(list(ascii_letters+digits+p),k = n))

print("\nYour new PWD:{0}{1}{0}Has been copied to clipboard!".format("\n"+min(n,80)*"="+"\n",c))

r.clipboard_clear()
r.clipboard_append(c)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

input("\nPress 'Return' to exit")
