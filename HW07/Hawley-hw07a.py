"""
James Hawley
10-14-2013
Howmwork#7a
"""

import sys

###   Functions   ###

def ConvertToBinary(x):
    """
    Receive a 1D list of numbers from the 2D list and sum the number 2
    being raised to each as a power.
    """
    mysum1 = 0
    for value in x:
        mysum1 = mysum1 + (2**value)

    """
    This code does the "remainder method" to convert
    the base 10 number to binary.
    """

    mysum2 = mysum1
    List1 = []
    while mysum1/2 != 0:
        List1.append(mysum1%2)
        mysum1 = mysum1/2
        if mysum1/2 == 0:
            List1.append(mysum1%2)

    """
    This code places zeros at the end to have a list that always
    has a certain number of elements in it.
    """

    while len(List1) != 19:
        aZero = 0
        List1.append(aZero)
            
    """
    This code puts the list in reverse.
    This is done because of how the remainder
    method works.  This will also conveniently place the
    zeros in the front.
    """
    List2 = []
    L = len(List1) - 1
    while L >= 0:
        List2.append(List1[L])
        L = L - 1

    """
    This code prints the spaces and X's
    """

    for value in List2:
        if value == 0:
            sys.stdout.write(" ")     ,
        elif value == 1:
            sys.stdout.write("X")     ,
            
    print "%10d" % mysum2

###   Main   ###

MyInitials = [[17,16,15,14,13,10,9,8,7,4,0],
            [15,10,7,4,0],
            [15,10,7,4,0],
            [15,10,9,8,7,4,3,2,1,0],
            [15,10,4,0],
            [18,15,10,4,0],
            [18,17,16,15,10,4,0]]
L1 = len(MyInitials)
a = 0

while a < L1:
    ConvertToBinary(MyInitials[a])
    a = a + 1


