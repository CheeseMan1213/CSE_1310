"""
playing with dictionaries
"""

#Remember that in dictionaries order does not matter because thet are hashed
d = {"cat" : "mouse",
     "frog" : "car",
     "house" : "bed",
     "James" : "Hawley",
     "Madison" : "friend"}

print d.items()#prints all keys and values
print len(d)#prints the number of elements in the dictionary
print d.keys()#prints just all the keys
print d.values()#prints just all the values
# create dictionaries with curly brackets, but referance them with square
#brackets
print d["cat"]#prints cat's value
print "#####"
print d.keys()
print "#####"

"""
Order does not matter.  The only problem you ran into was not being able to
print just one key.  
"""

def MySort(x):# receives a 1D list

    L1 = len(x) - 1
    Sorted = False

    while Sorted == False:
        Sorted = True
        a = 0
        while a < L1:
            if x[a].lower() > x[a + 1].lower():
                temp = x[a]
                x[a] = x[a + 1]
                x[a + 1] = temp
                Sorted = False
            a = a + 1

## when you use .lower() don't forget the parithisese
## uses parithisies for all built in functions


#in order to sort a dictionary, first make a list of its keys, that sort
#that list, then tell it to print the dictionary for each value in the
#sorted list and it will print them in order
#be careful to remember that capital letters come before lower case,
#so you may have to use the .lower function

print
print
print
keys = d.keys()# keys will be a list
print keys
MySort(keys)#apply python sort function to shadow modify the list
print keys

for k in keys:
    print k, d[k]# prints in alfabetical order of the keys

    
