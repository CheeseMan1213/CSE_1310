"""

"""

List = [10,6,8,7,3,5,4,1,2,3]
SortedList = []
print List
L1 = len(List) - 1
a = 0 # cycling variable
b = 0 # cycling variable
Finished = False

while Finished == False:
    while 0 <= a and a <= L1:
        if List[a+1] < List[a]:
            temp = List[a+1]
            List[a+1] = List[a]
            List[a] = temp
        else:
            Finished = True
        a = a + 1
