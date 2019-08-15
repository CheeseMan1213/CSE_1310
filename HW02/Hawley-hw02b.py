"""
James Hawley
09/07/2013
Homework#2
"""

"""
Write a program that prompts the user for three numbers (they
could be integers or
floats) and then prints the largest of the three numbers.
Do not use lists or the
max()
function.
"""

a = input("Enter a number:  ")
b = input("Enter a number:  ")
c = input("Enter a number:  ")

print

if a >= b and a >= c:
    print "The largest number is", a

elif b >= a and b >= c:
    print "The largest number is", b

elif c >= a and c >= b:
    print "The largest number is", c
