"""
James Hawley
09-23-2013
Howmwork#4
"""

ListA = [12, 3, 24, 30, 9, 11, 21, 8]
#print ListA

ListB = [] #List of divisor sums
ListC = [] #List of averages
a = 0
d = 1
mysum = 0
L1 = len(ListA) - 1

while 0 <= a and a <= L1:
    while 1 <= d and d <= ListA[a]:
        if ListA[a]%d == 0:
            mysum = mysum + d
        d = d + 1
    ListB.append(mysum)
    d = 1
    mysum = 0
    a = a + 1

#print ListB #List of divisor sums

r = 0
L2 = len(ListB) - 1

while 0 <= r and r <= L2:
    if r != 7:
        ListC.append((ListB[r] + ListB[r+1]) / 2.0)
    r = r + 1
    

#print ListC #List of averages


L3 = len(ListC) - 1

ListD = []
ListE = []
ListF = []

#print ListA in reverse
a = 7
while 0 <= a and a <= L1:
    ListD.append(ListA[a])
    a = a - 1
#print ListB in reverse
a = 7
while 0 <= a and a <= L2:
    ListE.append(ListB[a])
    a = a - 1
#print ListC in reverse
a = 6
while 0 <= a and a <= L3:
    ListF.append(ListC[a])
    a = a - 1

#print ListD #ListA in reverse
#print ListE #ListB in reverse
#print ListF #ListC in reverse

Tsum = 0
Tsum2 = 0

a = 0
while 0 <= a and a <= L2:
    Tsum = Tsum + ListB[a]
    a = a + 1

a = 0
while 0 <= a and a <= L3:
    Tsum2 = Tsum2 + float(ListC[a])
    a = a + 1

Average = Tsum2/len(ListC)

print

a = 0
while 0 <= a and a <= L1:
    print "%2d   " % ListD[a]     ,
    a = a + 1

print

a = 0
while 0 <= a and a <= L2:
    print "%2d   " % ListE[a]     ,
    a = a + 1

print

a = 0
while 0 <= a and a <= L3:
    print "  %1.1f" % ListF[a]     ,
    a = a + 1
    
print
print
print "Total sum = %d" % Tsum
print "Average of averages = %.2f" % Average



"""
d = input("Enter an number: ")
q = 1

while 1 <= q and q <= d:
    if d%q == 0:
        print q
    q = q + 1
"""
"""
while 0 <= a and a <= L1:
    print ListA[a]
    a = a + 1
"""
