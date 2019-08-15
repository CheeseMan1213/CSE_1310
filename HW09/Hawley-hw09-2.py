"""
James Hawley
11-02-2013
Howmwork#9
"""

#####     Function     #####

def CreateOneLargeList():
    a = 0
    d = []
    while a <= 99:
        b = "hw09-data-%02d.csv" % a# you need the zero %02d
        fp = open(b, "r")
        #c = fp.readlines()
        for line in fp:
            ss = line.strip()# srtip the line of white space and new lines and such
            AsAList = [ss]
            d.append(AsAList)# add the stripped line
        a = a + 1
        fp.close()
        
    return d
# d is the Large List

def Sort(LargeList): # receives the Large List
    L1 = len(LargeList)
    Sorted = False
    
    while Sorted == False:
        Sorted = True
        a = 0
        while a < (L1 - 1):
            tokens2 = LargeList[a][0].split(",")
            tokens3 = LargeList[a + 1][0].split(",")
            if tokens2[1] > tokens3[1]:
                temp = LargeList[a]
                LargeList[a] = LargeList[a + 1]
                LargeList[a + 1] = temp
                Sorted = False
            a = a + 1

def UniqueItemsPerMonth(LargeList):# this one is being used in another function
    #[January, car,str(0), phone,str(0),skillet,str(0)]
    ML = [["January"],
          ["February"],
          ["March"],
          ["April"],
          ["May"],
          ["June"],
          ["July"],
          ["August"],
          ["September"],
          ["October"],
          ["November"],
          ["December"]]
    
    
    for value in ML:# value is a 1D List
        for line in LargeList:# line is a 1D List
            tokens = line[0].split(",")
            if value[0] == tokens[0] and tokens[1] not in value:
                value.append(tokens[1])
                value.append("0")
        value.append("0")

    
        
    

    return ML
    
def FindIndex(word,RunningMonthList): # receives a single string
    #to find in a 1D list
    index = 0
    L1 = len(RunningMonthList)
    for value in RunningMonthList:
        if word == value:# each list is known to have only one element    
            return index
        else:
            index = index + 1
        
    return -1

def SumByMonth(LargeList):
    
    ML2 = UniqueItemsPerMonth(LargeList)# ML is a 2D List
    
    for line in LargeList:#line is a 1D List
        tokens = line[0].split(",")# always zero because it is just one string
        #for row in ML2
        a = 0
        L1 = len(ML2)#12
        L2 = len(ML2[a])
        while a < L1:
            if (tokens[0] in ML2[a]) and (tokens[1] in ML2[a]):
                Index = FindIndex(tokens[1],ML2[a])
                if Index != -1:
                    Index = Index + 1
                    ML2[a][Index] = float(ML2[a][Index]) + float(tokens[2])
                    ML2[a][Index] = "%.2f" % ML2[a][Index]
                    ML2[a][Index] = str(ML2[a][Index])
                    ML2[a][-1] = float(ML2[a][-1]) + float(tokens[2])
                    ML2[a][-1] = "%.2f" % ML2[a][-1]
                    ML2[a][-1] = str(ML2[a][-1])
            a = a + 1
        
            
    return ML2

#####     Main     #####

d = CreateOneLargeList()
Sort(d)
k = SumByMonth(d)
fp = open("JamesHW09File.csv", "w")

for line in k:
    count = 0
    pad = 0
    for letter in line[0]:
        count  = count + 1

    if count <= 4:
        pad = count + 7

    if count >= 5:
        pad = count + 6
            
    
    
    
    fp.write( ("%"+str(pad)+"s\n") % line[0])
    a = 1
    L1 = len(line) - 1
    while a < L1:
        fp.write( ("%-8s") % line[a])
        fp.write( ("%9s\n") % line[a + 1])
        a = a + 2
        
    fp.write( "-------------------\n")
    fp.write( ("%18s\n") % line[-1])
    fp.write("\n")


fp.close()

"""
for value in d:
    print value
"""
