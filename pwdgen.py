#!python3
#
# A practice program to generate passwords of a given lenght from alphanumeric and special characters.
#
# The menu could be extended to fit various common restrictions on acceptable passwords.
#

from random import choices
from string import punctuation, ascii_letters, digits
import pyperclip

n = int(input("How may characters should the password consist of?\n"))
'''if isinstance(n,(int,float)):
    n = int(n)
else:
    n = 12
    print("Not a valid value! Set to {0}\n".format(n))  
'''
q = (input("May it contain punctuation and special characters? (y/n)\n").lower())
if q == "y":
    p = punctuation
else:
    p = ""

c = "".join(choices(list(ascii_letters+digits+p),k = n))


pyperclip.determine_clipboard()
pyperclip.copy(c)

if not pyperclip.is_available():
    print("Copy functionality unavailable!")
    stat = ""
else:
    pyperclip.copy(c)
    stat = "Has been copied to clipboard!"

print("\nYour new PWD:{0}{1}{0}{2}".format("\n"+min(n,80)*"="+"\n",c,stat))


input("\nPress 'Return' to exit")
