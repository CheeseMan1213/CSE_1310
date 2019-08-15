"""
James Hawley
10-14-2013
Howmwork#8
"""

#####     Functions     #####

def CreateFiles(f): # recives a whole input file
    File1 = open("students.csv", "w")
    File2 = open("courses.csv", "w")
    UStud = []
    OrderNames = []
    Ordered = False
    UClas = []
    Stud = []
    Clas = []
    """
    This code creates a list of each line which will then be sorted.
    I credit my professor for the Bubble sort code.
    """
    for line in f:
        line = line.strip()
        OrderNames.append(line)
    """
    Bubble Sort.  This is done to put all the names next to eachother in order to work around
    a problem I encountered.
    This problem was answered next class but I did not work it in here because what I have still works.
    """
    L1 = len(OrderNames)

    while Ordered == False:
        Ordered = True
        a = 0
        while a < L1 - 1:
            if OrderNames[a] > OrderNames[a + 1]:
                temp = OrderNames[a]
                OrderNames[a] = OrderNames[a + 1]
                OrderNames[a + 1] = temp
                Ordered = False
            a = a + 1
    """
    Once the list was ordered I created some more lists for unique names and classes.
    """
    for line in OrderNames:
        tokens = line.split(",")
        if tokens[0] not in UStud:
            UStud.append(tokens[0])
        if tokens[1] not in UClas:
            UClas.append(tokens[1])
    """
    This for loops creates a list that places the sudent name followed by all their classes in the correct order all in one list.
    """
    for name in UStud:
        Stud.append(name)
        for line in OrderNames:
            if name in line:
                tokens1 = line.split(",")
                Stud.append(tokens1[1])

    """
    This for loop creates a list that places the class followed by all their students in the correct order all in one list.
    """
    for classs in UClas:
        Clas.append(classs) # the extra 's' is to work around the 'class' python keyword
        for line in OrderNames:
            if classs in line:
                tokens1 = line.split(",")
                Clas.append(tokens1[0])

    """
    The rest of the code writes to the two files I was instructed to create and places commas to seperate values.
    """
    b = 0
    L2 = len(Stud)
    
    while b < L2:
        if b == L2 - 1:
            File1.write( ("%s") % Stud[b])
        elif Stud[b + 1] in UStud:
            File1.write( ("%s\n") % Stud[b])
        elif Stud[b] in UStud:
            File1.write(("%s,") % Stud[b])
        else:
            File1.write(("%s,") % Stud[b])
        b = b + 1

    
    c = 0
    L3 = len(Clas)
    
    while c < L3:
        if c == L3 - 1:
            File2.write(("%s") % Clas[c])
        elif Clas[c + 1] in UClas:
            File2.write(("%s\n") % Clas[c])
        elif Clas[c] in UClas:
            File2.write(("%s,") % Clas[c])
        else:
            File2.write(("%s,") % Clas[c])
        c = c + 1
    
        
   
    File1.close()
    File2.close()  


#####     Main     #####


File = open("hw08-data.txt", "r")
# note: file handlers must match the ones used in the function
# note: file handlers must match the ones used in the function
CreateFiles(File)
File.close()
