"""
This code is practice with listing numbers

Remember: the range function lists number from the first number to one minus the second number,range(a,b-1),
that is the reason for the "b = b + 1" code.
"""

"""
#this is with the range function
a = input("Enter a Number:  ")
b = input("Enter a Number:  ")
b = b + 1

num = range(a,b)
print num
"""
"""
#this is with a while loop

num = 0
count = 1

while num < 10:
    num = num + 1
    count = count + 1
    print num
"""

print "This will find all the factors of the number you enter"
print
num = input("Enter your number:  ")
x = 1
count = 0
print

print "the factors of" , num , "are: "
while 1 <= x and x <= num:
    if num%x == 0:
        print x
        count = count + 1
    x = x + 1
    

print "This is", count, "numbers"    

