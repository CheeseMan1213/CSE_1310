"""
this code will find the average of a set of numbers
"""
#remember that you must start from zero in programming, the number first number in this set of
#numbers is in place zero.  :)

"""
num = [12, 34, 45, 56, 67, 890]
mysum = 0
count = 0

for j in num:
    mysum = mysum + j
    count = count + 1

print mysum, count
print mysum/count
"""


"""
This code will average any 6 numbers the user enters
"""

num1 = float(input("please enter a number: "))
num2 = float(input("please enter a number: "))
num3 = float(input("please enter a number: "))
num4 = float(input("please enter a number: "))
num5 = float(input("please enter a number: "))
num6 = float(input("please enter a number: "))
numT = [num1, num2, num3, num4, num5, num6]
mysum = 0
count = 0

for j in numT:
    mysum = mysum + j
    count = count + 1


print "the count is ", count
print "the total of the six numbers is ", mysum
print " the average of the six numbers is ", mysum/count
