"""
James Hawley
10-07-2013
Homework#6a
"""

#####     Functions     #####

def ColMax(a):
    c = 0
    L2 = len(a[c]) - 1
    NewList = []
    while 0 <= c and c <= L2:
        L1 = len(a) - 1
        mymax = 0
        r = 0
        while 0 <= r and r <= L1:
            mymax = mymax + a[r][c]
            r = r + 1
        c = c + 1
        NewList.append(mymax)
    return NewList

def Print1DList(a):
    for values in a:
        print "%5d" % values     ,

def Print2DList(a):
    r = 0
    L1 = len(a) - 1
    while 0 <= r and r <= L1:
        c = 0
        L2 = len(a[r]) - 1
        while 0 <= c and c <= L2:
            print "%4d" % a[r][c]     ,
            c = c + 1
        print
        r = r + 1

        
#####     main     #####
List1 = [[1,2,3],
         [4,5,6]]

List2 = [[10,20,30,40],
         [50,60,70,80],
         [90,100,110,120]]

print "the column sums of"
Print2DList(List1)
print "are"
Print1DList(ColMax(List1))
print
print "the column sums of"
Print2DList(List2)
print "are"
Print1DList(ColMax(List2))




"""
r = 0
L1 = len(List1)- 1
themax = 0
newList = []

while 0 <= r and r <= L1:
    c = 0
    L2 = len(List1[r]) - 1
    while 0 <= c and c <= L2:
        themax = themax + List1[c][r]
        c = c + 1
    newList.append(themax)
    r = r + 1

print themax
"""
"""
i = 0                       #4
mymax5 = TwoDList[0][0]
sum4 = 0
count4 = 0
while 0 <= i and i <= L1:
    j = a
    while  <= j and j <= 3:
        if TwoDList[i][j] > mymax5:
            mymax5 = TwoDList[i][j]
        sum4 = sum4 + TwoDList[i][j]
        count4 = count4 + 1
        j = j + 1
    i = i + 1
"""

##use List2
"""
def ColMax1(L): #L is the 2D List and c is the list index to stick with
    c = 0
    while 0 <= c and c <= len(L[c]) - 1:
    r = 0
    c = 0
    L1 = len(L) - 1
    L2 = len(L[c]) - 1
    NewList = []
    themax = 0
    while 0 <= r and r <= L1:
       c = 0
       themax = themax + L[r][c]
       r = r + 1
    NewList.append(themax)
    return NewList

print ColMax1(List2)
"""
## write a function that recives the c value and the 2Dlist




































































