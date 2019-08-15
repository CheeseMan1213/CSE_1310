"""
James Hawley
09-23-2013
Howmwork#4
"""

TwoDList = [[ 2.42, 11.42, 13.86, 72.32],         
            [56.59, 88.52,  4.33, 87.70],
            [73.72, 50.50,  7.97, 84.47]]


a = 0
L1 = len(TwoDList) - 1
L2 = len(TwoDList[0]) - 1
L3 = len(TwoDList[1]) - 1
L4 = len(TwoDList[2]) - 1


while 0 <= a and a <= L1:
    b = 0
    while 0 <= b and b <= L2:
        print "%5.2f" % TwoDList[a][b]     ,
        b = b + 1
    print
    a = a + 1


print "========================"

i = 0                       #1
mymax2 = TwoDList[0][0]
sum1 = 0
count1 = 0
while 0 <= i and i <= L1:
    j = 0
    while 0 <= j and j <= 0:
        if TwoDList[i][j] > mymax2:
            mymax2 = TwoDList[i][j]
        sum1 = sum1 + TwoDList[i][j]
        count1 = count1 + 1
        j = j + 1
    i = i + 1


i = 0                       #2
mymax3 = TwoDList[0][0]
sum2 = 0
count2 = 0
while 0 <= i and i <= L1:
    j = 1
    while 1 <= j and j <= 1:
        if TwoDList[i][j] > mymax3:
            mymax3 = TwoDList[i][j]
        sum2 = sum2 + TwoDList[i][j]
        count2 = count2 + 1
        j = j + 1
    i = i + 1


i = 0                       #3
mymax4 = TwoDList[0][0]
sum3 = 0
count3 = 0
while 0 <= i and i <= L1:
    j = 2
    while 2 <= j and j <= 2:
        if TwoDList[i][j] > mymax4:
            mymax4 = TwoDList[i][j]
        sum3 = sum3 + TwoDList[i][j]
        count3 = count3 + 1
        j = j + 1
    i = i + 1


i = 0                       #4
mymax5 = TwoDList[0][0]
sum4 = 0
count4 = 0
while 0 <= i and i <= L1:
    j = 3
    while 3 <= j and j <= 3:
        if TwoDList[i][j] > mymax5:
            mymax5 = TwoDList[i][j]
        sum4 = sum4 + TwoDList[i][j]
        count4 = count4 + 1
        j = j + 1
    i = i + 1



average1 = sum1/count1
average2 = sum2/count2
average3 = sum3/count3
average4 = sum4/count4

print "%5.2f %5.2f %5.2f %5.2f %s" % (mymax2, mymax3, mymax4,mymax5, "column max")
print "%5.2f %5.2f %5.2f %5.2f %s" % (average1, average2, average3,average4, "column average")


"""
#find max code

count = 1
g = []

while count <= 5:
    e = input("Enter a number: ")
    g.append(e)
    count = count + 1

h = 0
L5 = len(g)-1
mymax = g[0]
while 0 <= h and h <= L5:
    if g[h] > mymax:
        mymax = g[h]
    h = h + 1

print mymax
"""

"""
a = [1, 2, 10, 6, -9]
b = 0
L1 = len(a) - 1
TheMax = a[0]

while 0 <= b and b <= L1:
    if a[b] > TheMax:
        TheMax = a[b]
    b = b + 1

print TheMax
"""
