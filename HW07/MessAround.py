"""
James Hawley
10-14-2013
Howmwork#7a
"""

import sys
#sys.stdout.write(" ")

List1 = [[12, 3],
        [12, 3],
        [12, 3],
        [14, 13, 12, 9, 6, 3, 2, 1],
        [15, 12, 8, 7, 3, 0],
        [15, 12, 8, 7, 3, 0],
        [14, 13, 12, 9, 6, 3, 2, 1]]

List2 = [[11,10,9,7,6,5,3,0],
         [10,7,5,3,0],
         [10,7,5,3,0],
         [10,7,6,5,3,2,1,0],
         [10,7,3,0],
         [12,10,7,3,0],
         [12,11,10,7,3,0]]
    

def PrintSum(x): # receive a 1D List of numbers
    mysum = 0
    for value in x:
        mysum = mysum + (2**value)

    return mysum

"""
def ConvertToBinary(x):
    a = 0
    b = 2**a
    c = 0
    count= 0

    while c < x:
        c = c + 2**a
        count = count + 1
        a = a + 1
        
    return count

    while a < count:
        b = 2**a
        a = a + 1

"""
"""
## The remainder way

def ConvertToBinary2(x):
    List1 = []
    while x/2 != 0:
        List1.append(x%2)
        x = x/2
        if x/2 == 0:
            List1.append(x%2)

    #this code puts the list in reverse       
    List2 = []
    L = len(List1) - 1
    while L >= 0:
        List2.append(List1[L])
        L = L - 1

    for value in List2:
        if value == 0:
            sys.stdout.write(' ')     ,
        else:
            sys.stdout.write('X')     ,
    print
        
 """  

"""
z = input("Enter a number: ")
x = ConvertToBinary2(z)
L = len(x) - 1

while L >= 0:
    print x[L]     ,
    L = L - 1
"""

def ConvertToBinary3(x):
    """
    this code produces the base 10 number
    """
    mysum1 = 0
    for value in x:
        mysum1 = mysum1 + (2**value)

    """
    this code does the remainder method to convert
    to binary
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

    while len(List1) != 13:
        aZero = 0
        List1.append(aZero)
            
    """
    this code puts the list in reverse
    this is done because of how the remainder
    method works.
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
            print("%s") % (" ")     ,
        elif value == 1:
            print("%s") % ("X")     ,
    print "%8d" % mysum2

"""
ConvertToBinary3(List1[0])
ConvertToBinary3(List1[1])
ConvertToBinary3(List1[2])
ConvertToBinary3(List1[3])
ConvertToBinary3(List1[4])
ConvertToBinary3(List1[5])
ConvertToBinary3(List1[6])
"""
ConvertToBinary3(List2[0])
ConvertToBinary3(List2[1])
ConvertToBinary3(List2[2])
ConvertToBinary3(List2[3])
ConvertToBinary3(List2[4])
ConvertToBinary3(List2[5])
ConvertToBinary3(List2[6])


"""
for value in x:
    if value == 0:
        sys.stdout.write(' ')     ,
    else:
        sys.stdout.write('X')     ,
#print PrintBinary(List[0])
"""





