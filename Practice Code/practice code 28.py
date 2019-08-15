
"""

d = [[ 8, 7, 2, -3],
    [13, 6, 0, 16],
    [-4, 21, 3, 5]]

cmax = [ ]
rows = len( d )
cols = len( d[0] )

c = 0
while c < cols :
    mymax = d[0][c]
    r = 0
    while r < rows :
        if d[r][c] > mymax :
            mymax = d[r][c]
        r += 1
    print mymax ,
    cmax.append( mymax )
    c += 1
    
print
mymin = cmax[0]
for v in cmax :
    if v < mymin :
        mymin = v
        
print mymin
"""
"""
word = "ZDTAXXRZIYNU"

length = len( word )
i = 0
while i < length - 1 :
    if word[i] < word[i+1] :
        print word[i] ,
    i += 1
"""

"""
d = [1, 2, 3, 10, 9, 8, 4, 5, 6,9,10,12]
i = 2
L1 = len(d)

while i < L1:
    mysum  = d[i - 2]+d[i - 1]+d[i]
    average = mysum/3.0
    print "%.2f" % average     ,
    i = i + 1
"""

d = "George,Nancy,James,Theresa,Dan,Mark,Brandyn"
tokens = d.strip().split(",")
a = 0
L1 = len (tokens)

while a < L1:
    if a == L1 - 1:
        print ("%s") % (tokens[a])     ,
    else:
        print ("%s,") % (tokens[a])     ,
    a = a + 1
