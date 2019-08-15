"""
This is how to set multipal delimiters when spliting a string in python
you need the spaces too--- ; space the bar means there is not a space included in the 'is' string after the split
"""

a = "Beautiful, is; better*than\nugly"
import re
p = re.split("; |, |\*|\n", a)
print p
print
print

def isPeriod(a):
    IsP = False
    if "?" in a:
        IsP = True
    elif "." in a:
        IsP = True
    elif "!" in a:
        IsP = True
        
    return IsP

b = raw_input("Enter a sentance: ")
print isPeriod(b)
while isPeriod(b) == False:
    print "you must put punctuation at the end of your sentance."
    print "Either a '.' or '!' or '?'"
    print "Please try again."
    b = raw_input("Enter a sentance: ")

p = re.split(" |\?|\.|!", b)## in order to have the period as a delimiter, you must escape it
fix = p[0:len(p)-1:1]
print
print fix

#to fix the period problem you just create a new list
#by copying the the old list accept for the last character
#then print that new list
