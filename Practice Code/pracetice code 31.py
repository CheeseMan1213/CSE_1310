"""
practice with dictionaries within dictionaries
practice with recursion
recursion = having a function call itself
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
    #notice that no stopping condition is given
    # this will cause infinit recursion which will eventiall lead
    #to "Stack Overflow"
    print x
    return crash(x+1)

def SumUp(x):
    """
    Function able to handle summing all the numbers in a list
    no matter how many dimentions the list has. Using recursion.
    This works because the for loop continuously goes one level in
    each time it encounters a list.
    """
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

