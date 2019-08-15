"""
James Hawley
10-03-2013
Howmwork#5b
"""

List = ["1,10,100,1000",
    "-4,-3,-2,-1",
    "2,-3,5,-7,9,-11,13"]

def TheSum(n):
    tokens = List[n].split(",")
    mysum = 0
    for t in tokens:
        mysum = mysum + int(t)

    return mysum

def TheFormat(n):
    a = 1
    tokens = List[n].split(",")
    L1 = len(tokens)-1
    if tokens[0] >= 0:
        print "%d" % int(tokens[0])     ,
    else:
        print "%d" % int(tokens[0])     ,
    while 1 <= a and a <= L1:
        t = tokens[a]
        if int(tokens[a]) >= 0:
            print "+ %d" % int(t)     ,
        elif int(tokens[a]) <= 0:
            t = int(t) * (-1)
            print "- %d" % int(t)     ,
        a = a + 1
    return "="

print TheFormat(0)     ,
print TheSum(0)

print TheFormat(1)     ,
print TheSum(1)

print TheFormat(2)     ,
print TheSum(2)
