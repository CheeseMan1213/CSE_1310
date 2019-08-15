"""
This is practice code 20
This is me playing with the "try" and "except" functions
these allow python to except errors and continue on instead of crashing.

There is also use of the string.lower() function, used to temporarily make a string 
all lowercase.  This is useful for sorting.
"""


a = []
b = 0
try:
        if b != "stop" and b != '':
                b = raw_input("Enter a name: ")
                a.append(b)
except SyntaxError:
	print "You did not enter a name , please try again"

	
while b != "stop":
	try:
		b = raw_input("Enter a name: ")
		if b != "stop" and b != '':
			a.append(b)
	except SyntaxError:
		print "You did not enter a name , please try again"



c = 0
d = len(a)-1
while 0 <= c and c <= d :
	print a[c]     ,
	c = c + 1





d = ["Alfa", "Charlie", "Zulu", "Kilo", "foxtrot", "TanGo"]



size = len(a)
unsorted = True

while unsorted :
    unsorted = False
    i = 0
    while i < size-1 :
        if (a[i].lower() > a[i+1].lower()) and (a[i] != "stop") :
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            unsorted = True

        i += 1
print
print "The list sorted in alphabetic order is: "
print
print a




