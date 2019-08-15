"""
this code can find the max value is a given set of numbers
"""


"""
num = [12, 34, 1000, 56, 67, 789]
mymax = num[0]
print mymax

for j in num:
    if j > mymax:
        mymax  = j

print mymax
"""

"""
This code will find the max of any 6 numbers the user enters
"""


num1 = float(input("please enter a number: "))
num2 = float(input("please enter a number: "))
num3 = float(input("please enter a number: "))
num4 = float(input("please enter a number: "))
num5 = float(input("please enter a number: "))
num6 = float(input("please enter a number: "))
numT = [num1, num2, num3, num4, num5, num6]
mymax = numT[0]

print "the set of numbers you entered was: "
print numT

for j in numT:
    if j > mymax:
        mymax = j

print "the max number is ", mymax
