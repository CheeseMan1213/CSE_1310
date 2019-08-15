"""
this program will output the equation of a line that the user enters
using the slope formula.
"""

X1 = float(input("enter X1: "))
Y1 = float(input("enter Y1: "))
X2 = float(input("enter X2: "))
Y2 = float(input("enter Y2: "))
m = (Y2-Y1)/(X2-X1)
b = Y1 - m*X1


print "The line passes through", "(", int(X1), ",", int(Y1), ")", "and", "(", int(X2), ",", int(Y2), ")"       ,
print"and is of equation", "y = ", m, "x", "+", b
