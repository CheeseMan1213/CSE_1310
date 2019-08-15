"""
James Hawley
10-14-2013
Howmwork#7a
"""

import sys

###   Functions   ###

def ConvertToBinary(x):
    """
    receive a 1D List of numbers and sum the number 2
    being raised to each as a power
    """
    mysum1 = 0
    for value in x:
        mysum1 = mysum1 + (2**value)

    """
    This code does the remainder method to convert
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
    has 13 elements
    """

    while len(List1) != 17:
        aZero = 0
        List1.append(aZero)
            
    """
    this code puts the list in reverse
    this is done because of how the remainder
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

MyInitials2 = [[11,10,9,7,6,5,3,0],
            [10,7,5,3,0],
            [10,7,5,3,0],
            [10,7,6,5,3,2,1,0],
            [10,7,3,0],
            [12,10,7,3,0],
            [12,11,10,7,3,0]]

MyInitials = [[15,14,13,12,11,9,8,7,6,4,0],
            [13,9,6,4,0],
            [13,9,6,4,0],
            [13,9,8,7,6,4,3,2,1,0],
            [13,9,4,0],
            [16,13,9,4,0],
            [16,15,14,13,9,4,0]]




ConvertToBinary(MyInitials[0])
ConvertToBinary(MyInitials[1])
ConvertToBinary(MyInitials[2])
ConvertToBinary(MyInitials[3])
ConvertToBinary(MyInitials[4])
ConvertToBinary(MyInitials[5])
ConvertToBinary(MyInitials[6])



