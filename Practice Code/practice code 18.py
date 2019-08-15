a = 10
mysum =0
while 10 <= a and a <= 100:
    if a%4 == 0 or a%6 == 0:
        if a%4 == 0 and a%6 != 0:
            mysum = mysum + a
        elif a%4 != 0 and a%6 == 0:
            mysum = mysum + a
    a = a + 1

print mysum
