"""
playing with and, or , not logic statments
"""

a = input("enter a number:  ")
b = input("enter a number:  ")
c = input("enter a number:  ")
print

if a == 12 and b == 24 and c == 36:
    print "cool beans"
if a != 12 or c != 36:
    print "this is not cool"
else:
    print "this is still cool"

if a is not b:
    print "a is not b"
else:
    print "a is b"

print ":-)"
