"""
James Hawley
10-03-2013
Howmwork#5a
"""

def countTokens(n):
    count = 0
    tokens = List[n].split(",")
    for t in tokens:
        count = count + 1
    return count

def countChar(n):
    tokens = List[n].split(",")
    count = 0
    for t in tokens:
        for c in t:
            count = count + 1
    return count

def TokMaxChar(n):
    tokens = List[n].split(",")
    L3 = len(tokens) - 1
    a = 0
    count = 0
    themax = 0
    while 0 <= a and a <= L3:
        count = 0
        for c in tokens[a]:
            count = count + 1
        if count > themax:
            themax = count
            Srtmax = tokens[a]
        a = a + 1

    return Srtmax

List = ["cat,elephant,horse,anteater,giraffe",
    "Impala,Mustang,Thunderbird,Viper",
    "123.4567,987654,99.99%"]
L1 = len(List)-1

t = 0
while 0 <= t and t <= L1:
    print "token count = %d," % countTokens(t)     ,
    print "character count = %d," % countChar(t)    ,
    print "%s has the most characters" % TokMaxChar(t)
    t = t + 1









