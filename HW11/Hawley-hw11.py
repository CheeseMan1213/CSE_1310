"""
James Hawley
11-16-2013
Howmwork#11
"""

import urllib

#####     Funtions     #####
def FindIndex(a,b):#(search for, the list to look in)
    """
    receives what to search for and where to search for it (Degree, Dict[key])
    """
    L1 = len(b)
    g = 0
    while g < L1:
        if a == b[g]:
            return g
        else:
            g = g + 1
    return -1

def PredictDegree(Deg,Stu):# receives (DegreesFile, StudentFile)
    """
    assuming that it will always be such that it is just either a 'degree, course'
    or 'student, course'.  When tokenizing, tokens will always have just two elements.
    Try using a dictionary

    sudo data structure:
    StudCor = {"Name1" : [degree name, count, degree name, count.. and so on],
                        "Name2" : [degree name, count, degree name, count....],
                        "Name3" : [degree name, count, degree name, count....]}
                            and so on
    I only want to add one to a persons degree plan count if...
    """
    StudCor = {}# empty dictionary
    
    for line1 in Stu:#lookes at all strings
        """
        will cycle through the students once, but cycle through all the degrees once for
        each student.
        """
        tokens1 = line1.strip().split(",") #tokenizes one string at a time
        if tokens1[0] not in StudCor:# builds dictionary on unique names
            """
            if key(student name) not there, add it with an
            empty list as a value, if there do nothing.
            """
            StudCor[tokens1[0]] = []
        for line2 in Deg:# looks at all strings
            """
            Then compair to Degrees.csv, 
            """
            tokens2 = line2.strip().split(",")#tokenizes one string at a time
            if tokens2[0] not in StudCor[tokens1[0]]:
                """
                if the degree is not in the list add it and a zero to the list
                """
                StudCor[tokens1[0]].append(tokens2[0])
                StudCor[tokens1[0]].append(0)# zero is appended at an int.(this is the count)
            else:# if there, just add to the count
                if tokens2[1] == tokens1[1]:
                    """
                    if the class in the current line in the degrees.csv is equal to a class that a student
                    is taking, find its respective count (the number in front of it) and add one
                    to it
                    """
                    Index = FindIndex(tokens2[0], StudCor[tokens1[0]])#(search for,search here)
                    StudCor[tokens1[0]][Index + 1] = StudCor[tokens1[0]][Index + 1] + 1

    """
    print "##########"
    for key in StudCor:
        print key, StudCor[key]
    print "##########"
    """
    return StudCor

def PrintOutput(g): # receives competed StudCor dictionary to print
    DicKeys = g.keys()#grabs keys
    DicKeys.sort()#sorts the keys alfabeticly
    for key in DicKeys:
        a = 1 # starting at one because I know where the numbers are
        mymax = g[key][1] # inital value for the max
        L1 = len(g[key])
        DegreePlan = g[key][0]# initial value

        while a < L1:
            if g[key][a] > mymax:
                mymax = g[key][a]# you might not be printing the number but you do need it
                DegreePlan = g[key][a - 1]# a-1 will be the string before the number
            a = a + 2

        print ("%s is a %s major") % (key, DegreePlan)# you are in a for loop here. The indentation
        #is correct, it will print once for each key(student).

#####     Main     #####
            
# grabs data
fp = urllib.urlopen("http://omega.uta.edu/~darin/CSE1310/degrees.csv", "r")
DegreesFile = fp.readlines()# is  1D list with each line as its own single string
fp.close()
fp = urllib.urlopen("http://omega.uta.edu/~darin/CSE1310/hw11-data.csv", "r")
StudentFile = fp.readlines()# is  1D list with each line as its own single string
fp.close()
# create data structure and nessary additions to the count
StudCor = PredictDegree(DegreesFile, StudentFile)
#prints data with student and degree plan with highest count
PrintOutput(StudCor)
