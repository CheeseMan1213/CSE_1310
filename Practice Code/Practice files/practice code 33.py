"""
CSE-1310 Final Exam Practice
problem #24
"""
"""
fp = open("movies.csv", "r")
MovL = fp.readlines()
fp.close()
MovD = {}

for line in MovL:
    tokens = line.split(",")
    inList = []
    inList.append(tokens[1])
    inList.append(tokens[2])
    MovD[tokens[0]] = inList

#MovD complete

find = raw_input("Please enter a search topic: ")
for title in MovD:
    if find in MovD[title][0] and int(MovD[title][1]) % 2 == 0:
        print title
"""
"""
CSE-1310 Final Exam Practice
problem #1
"""

def clean( line ) :
    newline = [ ]
    t = line.strip().split(',')
    for x in t :
        newline.append( int(x) )
    return newline

def fx( d ) :
    rows = len( d )
    cols = len( d[0] )
    c = 0
    while c < cols :
        sum = 0
        r = 0
        while r < rows :
            sum += d[r][c]
            d[r][c] = sum
            r += 1
        c += 1

##### main #####
data = [ ]
fp = open("file3-5.csv", "r")
for line in fp :
    data.append( clean(line) )
fp.close()
fx( data )
for line in data :
    print line
