"""
This is a number guessing game that will let the player guess 7 times to find the right number
"""

import random

snum = random.randint(1,100)
print snum

count = 0
guess = -1

while count != 7:
    count = count + 1
    print count


count = 1
while count != 7:
    while guess != snum:
        guess = input("Enter your guess:  ")
        if guess == snum:
            print "You got it!"
        elif guess < snum:
            print "Too low"
        else:
            print "Too high"
    count = count + 1
print " The count is ", count





    
    
"""
    while guess != snum:
        guess = input("Enter your guess:  ")
        if guess == snum:
            print "You got it!"
            #count = count + 1
        elif guess < snum:
            print "Too low"
            #count = count+ 1
        else:
            print "Too high"
"""
    
    
        
