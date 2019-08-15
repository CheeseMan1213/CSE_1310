"""


"""

n = input("Enter a number: ")

#####  Function #####

def isPrime (n):
    a = 1
    count = 0
    prime = False
    while 1 <= a and a <= n:
        if n%a == 0:
            count = count + 1
        a = a + 1
    if count == 2:
        prime = True
    return prime

##### main #####

b = 1

while 1 <= b and b <= n:
    if isPrime(b):
        print b     ,
    b = b + 1
