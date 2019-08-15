"""
hfksd
"""

num = input("Enter a number: ")
x = 1
while x <= num:
    t = 1
    while t <= x:
        print "%2d" %x    ,
        t = t + 1
    print    
    x = x + 1
