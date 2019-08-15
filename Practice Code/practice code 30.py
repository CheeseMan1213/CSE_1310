"""
practice with dictionaries within dictionaries
practice with recursion
"""

# form of last name,first name, and a number
Names = {"Hawley" : {"James" : 1},
         "Smith" : {"John" : 2},
         "Perry" : {"Katie" : 3},
         "Lockhart" : {"Tifa" : 4},
         "Gainsborough" : {"Aerith" : 5},
         "Summers" : {"Buffy" : 6},
         "Hawley" : {"James" : 2}}


def TestRecursion(x):
    if x > 100:# this is you stopping condition
        return x
    return TestRecursion(x*2)
def crash(x):
    print x
    return crash(x+1)

def SumUp(x):
    mysum = 0
    for value in x:
        if type(value) == type([]):
            mysum = mysum + SumUp(value)
            
        else:
            mysum = mysum + value

    return mysum

#c = input("Please enter a number: ")
#x = crash(8)
"""
d = 0
while d <= 100:
    print d
    d = d + 1
"""
#84
numbers1 = [1,2,3,4,5,6,7,8,9,8,7,6,5,6,4,3,]
numbers2 = [1,[2,3],4,5,[6,7,8,9,8,7],6,[[[5,[6,4]]]],3]
print SumUp(numbers2)

