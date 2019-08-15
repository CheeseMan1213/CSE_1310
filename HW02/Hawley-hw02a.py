"""
James Hawley
09/04/2013
Homework#2
"""

num = input("Please type an integer:  ")

if num == 0:
    print "zero"
elif num > 0:
    print "The number is positive"
    if num%5 ==0:
        print "The number is divisible by 5"
    else:
        print "The number is not divisible by 5"
elif num < 0:
    print "The number is negative"
    if num%5 ==0:
        print "The number is divisible by 5"
    else:
        print "The number is not divisible by 5"
        

