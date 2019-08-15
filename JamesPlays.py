#
#This page will contain various instructions for using python.




#this is a comment(every line)
#this is a comment too
""" multi-line
this is a comment too
this is a comment too
this is a comment too
"""

#if statments must have a colon and the end of them

# the pythagoren theorm
"""
import math

a = -12
b = 5
c = math.sqrt(a**2 + b**2)
print c
"""

#the quadratice formula
"""
import math

a = input('Enter variable a:')
b = input('Enter variable b:')
c = input('Enter variable c:')

x = (-b + math.sqrt(b**2 - 4 * a * c))/2*a
print float(x)
#print (str("hello") + float(x))

x2 = (-b - math.sqrt(b**2 - 4 * a * c))/2*a
print float(x2)
#print (str("hello") + float(x2))
"""

#Keep in mind that any condition that evaluates to a
#nonzero value is considered true.

#Also, keep in mind that any condition that evaluates to a
#zero value is considered false.

"""
a = 99
b = 0
c = 74
if a or b :
    print "first"
else:
    print "second"
if a and c :
    print "third"
else:
    print "fourth"
if not a :
    print "fifth"
else:
    print "sixth"
if (a and b) or c :
    print "seventh"
else:
    print "eighth"
if (not c) :
    print "nineth"
else:
    print "tenth"
"""

x = 4
if x > 3 :
    print "one"
    x += 2
    if x < 10 :
        print "two"
        x = 2*x + 1
        if 15 < x and x < 25 :
            print "three"
            x = x - 1
            if x < 100 :
                print "four"
            else :
                print "five"
        else :
            print "six"
    else :
        print "seven"
else :
    print "eight"

    
