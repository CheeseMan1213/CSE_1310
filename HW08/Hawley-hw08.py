"""
James Hawley
10-14-2013
Howmwork#8
"""
import sys
#sys.out.write()

#####     Functions     #####

def CreateFiles(f): # recives a whole input file
    UStud = []
    OrderNames = []
    Ordered = False
    UClas = []
    Stud = []
    Clas = []

    for line in f:
        line = line.strip()
        OrderNames.append(line)

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
            
    for line in OrderNames:
        tokens = line.split(",")
        if tokens[0] not in UStud:
            UStud.append(tokens[0])
        if tokens[1] not in UClas:
            UClas.append(tokens[1])

    for name in UStud:
        Stud.append(name)
        for line in OrderNames:
            if name in line:
                tokens1 = line.split(",")
                Stud.append(tokens1[1])


    for classs in UClas:
        Clas.append(classs)
        for line in OrderNames:
            if classs in line:
                tokens1 = line.split(",")
                Clas.append(tokens1[0])
    """
    for value in Stud:
        if value not in UStud:
             
            print ("%s") % value     ,
            print
        else:
            print
            print ("%s,") % value     ,

    print
    print
    print

    for value1 in Clas:
        if value1 not in UClas:
            print ("%s") % value1     ,
        else:
            print
            print ("%s") % value1    ,
    """

    print
    print "*****"
    b = 0
    L2 = len(Stud) - 1
    while b < L2:
        if b == L2:
            print ("%s") % Stud[b]     ,
        if Stud[b + 1] in UStud:
            print ("%s") % Stud[b]
        elif Stud[b] in UStud:
            print("%s,") % Stud[b]     ,
        else:
            print ("%s,") % Stud[b]     ,
        b = b + 1
        
    print
    print 
    print
    
    c = 0
    L3 = len(Clas) - 1
    while c < L3:
        if Clas[c + 1] in UClas:
            print ("%s") % Clas[c]
        elif Clas[c] in UClas:
            print("%s,") % Clas[c]     ,
        else:
            print ("%s,") % Clas[c]     ,
        c = c + 1
    
        
        
   
    


#####     Main     #####


File = open("hw08-data.txt", "r")
CreateFiles(File)
File.close()
