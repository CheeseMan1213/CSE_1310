"""


"""

"""
a = 1

while a <= 20:
    b = 10**a
    print b
    print type(b)
    print
    a = a + 1

print "again"
c = 10**1000
print type(c)
"""

# Truples and Lists

# the difference is that List can be modified and Truples cannot
# trubles will be useful keep the list from being modified
#can also prevent the shadow copy issue, kind of

s = [1,2,3,4,5]
w = (1,2,3,4,5)
print type(s)
print type(w)
s[0] = 16
print s
print
#w[0] = 17  # TypeError: 'tuple' object does not support item assignment

# you can still pick out specific values from a truple
print w[4] # will give you the number
