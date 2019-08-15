"""
this program will prompt the user 6 times for a number and then tell if the number is odd or even
"""


count = 0
#remember count started at zero and zero counts too[0,1,2,3,4,5] is six numbers
while count <=5:
    num = input("Enter a number:  ")
    if num%2 == 0:
        print
        print "the number is even"
        print
        count = count +1
    else:
        print
        print "the number is odd"
        count = count +1
        print
