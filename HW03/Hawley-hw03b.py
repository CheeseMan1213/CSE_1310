""""
James Hawley
09-12-2013
Homework#3
"""

a = input("Enter the first number:  ")
b = input("Enter the second number:  ")
mysum = 0
count = 1
print

if a > b:
    print "The first number must be less than the second number"
    print
else:  
    while a <= a and a <= b:
        print "%2d," % a        ,
        mysum = mysum + a
        print "%3d," % mysum    ,
        myavg = mysum/float(count)
        print "%3.2f" % myavg
        a = a + 1
        count = count + 1
