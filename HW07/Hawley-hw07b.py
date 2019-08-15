"""
James Hawley
10-14-2013
Howmwork#7b
"""

###   Functions   ###
def MinMaxSinUnsin(b): # receives an int value
    """
    There is no math for the unsigned in min.
    If it can only be positive, then the smallest
    value will always be zero
    """
    UnSignedMin = 0
    UnSignedMax = (2**b) - 1
    SignedMin = (-(2)**(b-1))
    SignedMax = 2**(b-1) - 1

    print ("%2d%11d%12d%13d%13d") % (b,UnSignedMin, UnSignedMax, SignedMin, SignedMax)

def Bbits(n): # receives an int value
    """
    This code will produce the number in binary
    using the remainder method
    """
    c = n# to produce the value n at a later time because it will be modified
    List1 = []
    while n/2 != 0:
        List1.append(n%2)
        n = n/2
        if n/2 == 0:
            List1.append(n%2)

    """
    This code will use variable b to count the number of bits
    """

    b = 0
    for value in List1:
        b = b + 1

    UnSignedMax1 = (2**b) - 1
    b = b - 1
    UnSignedMax2 = (2**b) - 1
    b = b + 1

    
    print("%6d%9d%15d%13d") % (c,b,UnSignedMax2,UnSignedMax1)
    


###   Main   ###

List1 = [2,3,8,10,16,20,32] # These integers represent a number of bits
List2 = [2,10,20,100,1000,999999] # int value to be stored as an unsigned int

print ("%s%15s%24s") %("number", "unsigned", "signed")
print ("%s%6s%12s%13s%13s") % ("of bits", "min", "max","min","max")

for value in List1:
    MinMaxSinUnsin(value)

print 


print ("%18s%13s%13s") %("unsigned", "max value", "max value")
print ("%s%11s%14s%11s") % ("number", "b bits", "b-1 bits","b bits")

for value in List2:
    Bbits(value)

