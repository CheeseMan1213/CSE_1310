"""


"""
"""
count = 0
a = 1
mysum = 0
while a <= 5:
    n = input("Enter a floating point number: ")
    n = float(n)
    mysum = mysum + n
    count = count + 1
    average = mysum/count
    print "The average of the first %d numbers is %.2f" % (count,average)
    a = a + 1
"""

def Pnum(n):
    a = 1
    mysum = 0
    while 1 <= a and a <= n:
        if n%a == 0 and a != n:
            mysum = mysum + a
        a = a + 1
    if mysum == n:
        return True
    else:
        return False


a = 1
while a <= 1257788:
    if Pnum(a) == True:
        print a     ,
    a = a + 1
"""
print
p = 2**12*(2**13-1)
print p
print Pnum(p)
"""
