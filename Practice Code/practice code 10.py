"""
This is me playing with formate specifiers
"""
"""
while True :
    n = input("\nEnter a positive integer (negative to stop):  ")

    if n < 0 :
        break

    if not isinstance(n, int) :
        print "error: you did not enter an integer"
        continue

    if n < 2 or 10 < n :
        print "error: that number is not in the valid range"
        continue

    if n == 2 or n == 3 or n == 5 or n == 7 :
        print n, "is prime"
    else:
        print n, "is not prime"
"""
import math

a = 12    #"%d" or "%f" or "%c" or "%s"
b = 14
c = 16
d = "James"
f = math.pi

print "%012d" % (a)
print "%4d" % (b)
print "%5d" % (c)
print "%9s" % (d)
print
