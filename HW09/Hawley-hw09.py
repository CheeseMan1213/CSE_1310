"""
James Hawley
11-02-2013
Howmwork#9
"""


def CreateOneLargeList():
    a = 0
    d = []
    while a <= 99:
        b = "hw09-data-%02d.csv" % a# you need the zero %02d
        fp = open(b, "r")
        c = fp.readlines()
        for line in c:
            ss = line.strip()# srtip the line of white space and new lines and such
            d.append(ss)# print the stripped line
        a = a + 1
        fp.close()
        
    return d
# d is the Large List

def Sort(LargeList): # Recives the Large List
    L1 = len(LargeList)
    Sorted = False
    
    while Sorted == False:
        a = 0
        while a < (L1 - 1):
            if LargeList[a + 1] > LargeList[a]:
                temp = LargeList[a]
                LargeList[a] = LargeList[a + 1]
                LargeList[a + 1] = temp
            else:
                Sorted = True
            a = a + 1
            

#d = CreateOneLargeList()
k = ["zoo,house,car,aarvark,cow,lamp,lamma"]
Sort(k)
for line in d:
    print line


    


"""
data = fp.readlines()

for line in data:
    line.strip()
    print line     ,

fp.close()
"""

d = [8, 14, 3, 5, 2]

size = len( d )
unsorted = True

while unsorted :
    unsorted = False
    i = 0
    while i < size-1 :
        if d[i] > d[i+1] :
            temp = d[i]
            d[i] = d[i+1]
            d[i+1] = temp
            unsorted = True

        i += 1

print d
