"""
This is me playing with lists
"""
"""
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print d
#d[0] = 12
print d
size = len(d)
print size
print d[size-1]
print d[-1]
print d[4 : ]
x = d[ : ]
print x
d.append(2000)
print d
"""

#average my grades
grades = []
x = input("Enter your grades(use negative number to exit): ")
while x >=0:
    grades.append(x)
    x = input("Enter your grades(use negative number to exit): ")
    
print "The grades you entered where"
print grades
length = len(grades)
y = 1
avg = 0
mysum = 0
while y < length:
    mysum = mysum + grades[x]
    y = y + 1

avg = mysum/float(length)
print "your class average is", avg


"""
k = [100, 95, 97, 75, 89]  #91.2
mysum = 0
x = 0
y = len(k)   # 5

while x < y:
    mysum = mysum + k[x]
    x = x + 1

print mysum
print mysum/float(y)
"""
"""
while x <= y-1:
    add = k[x]
    mysum = mysum + add
    x = x + 1
"""
"""
print mysum   #456
"""
"""
k = [100, 95, 97, 75, 89]
a = k[0] + k[1] + k[2] + k[3] + k[4]
x = 0
print a


while x < len (k):
    print k[x]
    x = x + 1
"""
