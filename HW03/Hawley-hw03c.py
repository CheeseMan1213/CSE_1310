"""
James Hawley
09/12-2013
Howmwork#3
"""

num = input("Enter an number: ")
x = 1
if num < 1:
    print "The number you entered is too low"
else:
    while x <= x and x <= num:
        count = 1
        while count <= x:
            print "%2d" % x    ,
            count = count + 1
        print
        x = x + 1
