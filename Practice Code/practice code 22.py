"""



"""

"""
import sys

a = 123
b = 456
c = 789
print a, b, c
print
print "This one"
print ("%d%d%d") % (a, b, c) #this is the code that worked first
print
print "This one"
sys.stdout.write(a)     ,#
sys.stdout.write(b)     ,# this is the second one that worked
sys.stdout.write(c)      #


print

a = 1

while 0 <= a and a <= 10:
    print a     ,
    a = a + 1


print
print
a = 1
print "This one."
while 0 <= a and a <= 9:
    sys.stdout.write(a)     ,# the third one that worked
    a = a + 1
"""
""" # factor program
d = input("Enter a number: ")# find divisors code on the fly
s = 1
while 1 <= s and s <= d:
    if d%s == 0:
        print s     ,
    s = s + 1
""" 
w = "James, Katy Perry, House, carrs, motel"
tok = w.split(',', 'P') #remember that .split creates a list
print tok

for t in tok:
    print t   ,

print

for t in tok:
    print t.strip()
