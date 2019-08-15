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
        try:
            fp = open(b, "r")
        except IOError:
            a = a + 1
            continue
        #c = fp.readlines()
        for line in fp:
            ss = line.strip()# srtip the line of white space and new lines and such
            AsAList = [ss]
            d.append(AsAList)# add the stripped line
        a = a + 1
        fp.close()
        
    return d
# d is the Large List

def UniqueItemsPerMonth(LargeList):
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

def PrintAndSumByMonth(LargeList):
    
    ML2 = UniqueItemsPerMonth(LargeList)
    
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
                    #print"#####"
                    #print row[b], tokens[2]
                    #print"#####"
            a = a + 1
            
    return ML2

#####     Main     #####
d = CreateOneLargeList()
k = PrintAndSumByMonth(d)

for line in k:
    print line[0]
    a = 1
    L1 = len(line) - 1
    while a < L1:
        print line[a]    ,
        print line[a + 1]
        a = a + 2
    print

"""
for value in d:
    print value
"""
