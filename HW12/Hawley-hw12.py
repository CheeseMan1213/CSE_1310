"""
James Hawley
11/22/2013
Homework#12
"""
"""
-you will have to tell the computer to ignore the commented out lines in the file '#'
-also, to be able to handle the third delimitd value(the prerequ) three ways:
if it is not there at all/if there is only one/for multiples(the vertical bar)
-also to be able to handle the notes that are sometimes at the end of the line(potetial last value)
-make sure you create "your own" 'completed.txt' file.
-sort output in alpfabetical order correctly and ignoring capitalization 'A' before 'B'
but not 'B' before 'a'. use '.lower()'
-you are printing->'what you have completed' , 'Then 'All' of what is left' , 'Then only what is
left that you have met the prerequisits for'.   "Three things"
-make sure you account for the fact that a student must pass the professional line before they
can take and 4000 level courses
"""
        #####       Functions       #####
def MySort(f):# recives a 1D list of strings to sort
    L1 = len(f) - 1
    Sorted = False
    
    while Sorted == False:
        a = 0
        Sorted = True
        while a < L1:
            if f[a].lower() > f[a + 1].lower():
                temp = f[a]
                f[a] = f[a + 1]
                f[a + 1] = temp
                Sorted = False
            a = a + 1

def MyPrint(LN):# receives a single string to print
    """
    this will print but ignore comments '#'
    """
    if "#" not in LN:
        print ("     %s") %  line     ,

def AllClassesLeft(MasterList,CousreComplete):
    """
    function receives the two files, the students competed courses list and the master list
    for the specific degree plan.
    I only want it to print the current MasterList course if it looks at the whole competed
    List and finds no match, which means the course still remaining.
    the first part of this function generates the Remaining course list.
    the other part also similtainiously creates the dictionary "WhatsLeftList"
    **Shell data structure->
    WhatsLeftList = {course name : [[prerqu classes, if any or a zero],note = as a string],
                                 course name : [[prerqu classes, if any or a zero],or nothing if there is no note],
                                 course name : [[prerqu classes, if any or a zero],note = as a string],
                                 course name : [[prerqu classes, if any or a zero],note = as a string]}
    if there is a note the value list will have 2 elements
    if there is no note then the value list will have only one element
    """
    
    WhatsLeftList = {}
    for line1 in MasterList:
        MatchFound = False
        if "#" in line1:
            continue
        tokens1 = line1.strip().split(",")
        for line2 in CousreComplete:
            if "#" in line2:
                continue
            tokens2 = line2.strip().split(",")
            if tokens1[0] == tokens2[0]:
                MatchFound = True
        if MatchFound == False:
            print ("     %s") % tokens1[0]
            WhatsLeftList[tokens1[0]] = []
            if tokens1[2] != (""):# potential prerequ part
                if "|" in tokens1[2]:
                    tokens3 = tokens1[2].split("|")
                    WhatsLeftList[tokens1[0]].append(tokens3)
                else:
                    WhatsLeftList[tokens1[0]].append([tokens1[2]])
            else:
                WhatsLeftList[tokens1[0]].append([0])
            if  tokens1[3] != (""):# that means that there is a note
                WhatsLeftList[tokens1[0]].append(tokens1[3])
                
            
            # append the course, the prerequs(if any), the notes(if any)
    return WhatsLeftList


def StudentAvalibleClasses(CousreComplete,WhatsLeftList):
    """
    I only want it to print the course and note , if any, if the prerqus have been met
    """
    keys = WhatsLeftList.keys()
    MySort(keys)
    for classs in keys:
        L1 = len(WhatsLeftList[classs][0])
        a = 0
        count = 0

        if WhatsLeftList[classs][0][0] == 0:
            if len(WhatsLeftList[classs]) == 2:# that means there is a note
                print ("       %s (%s)") % (classs, WhatsLeftList[classs][1])
            else:
                print ("       %s") % (classs)

        else:            
            while a < L1:
                for line in CousreComplete:
                    if "#" in line:
                        continue
                    if WhatsLeftList[classs][0][a] == line.strip():
                        count = count  + 1
                
                a = a + 1
            if count == L1:
                if len(WhatsLeftList[classs]) == 2:
                    print ("       %s (%s)") % (classs, WhatsLeftList[classs][1])
                else:
                    print ("       %s") % (classs)
                    
        
        #####       Main        #####
fp = open("completed.txt","r")
CousreComplete = fp.readlines()
fp.close()
fp = open("bscs-2013.csv","r")
MasterList = fp.readlines()
fp.close()

MySort(CousreComplete)
MySort(MasterList)
"""
MySort(d)
for value in CousreComplete:
    print value     ,
"""


print "Courses Completed"
print"-"*24
for line in CousreComplete:
    MyPrint(line)

print
print


print "Courses Remaining"
print"-"*24
WF = AllClassesLeft(MasterList,CousreComplete)
"""
print "#################"
for key in WF:
    print key, ":",  WF[key]
print "#################"
"""
print
print "Courses Eligible To Take"
print "-"*31
StudentAvalibleClasses(CousreComplete,WF)
