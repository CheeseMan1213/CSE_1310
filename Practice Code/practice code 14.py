"""
09/18/2013
practice finding the max and min numbers in a list
"""
List = [2000, 45, 19, 23, 56, 23, 1001, 101, -12, 1000]
length = len(List)
i = 0
mymax = List[0]
mymin = List[0]
while i <= length - 1:
    if List[i] > mymax:
        mymax = List[i]
    if List[i] < mymin:
        mymin = List[i]
    i = i + 1
print "The max number is, %d" % (mymax)
print "The min number is, %d" % (mymin)
