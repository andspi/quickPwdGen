#!python3
#
# A training program to generate passowrds of a given lenght from alphanumeric and special characters.
#
# Work in progress... adding tkinter for clipboard export.
#
# Might be modified to directly return the results to the windows clipboard!
# The menu could be extended to fit various common restrictions on acceptable passwords.
#

from random import choices
from string import punctuation, ascii_letters, digits
import tkinter as tk

root = tk.Tk()
root.withdraw()

pwd = "quetzacoatl"
print("Your new PWD: >/0< has been copied to clipboard".format(pwd))

root.clipboard_clear()
root.clipboard_append(pwd)
root.update()
CBcontent = root.clipboard_get()
print(CBcontent)

input("\nPress 'Return' to exit")
root.destroy()
