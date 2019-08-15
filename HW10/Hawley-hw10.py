"""
James Hawley
11-09-2013
Howmwork#10
"""

import math
##### Functions #####
def CalculateDistance(x1,y1,x2,y2):
    Distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    return Distance

def MySort(x):# receives a 1D List

    L1 = len(x) - 1
    Sorted = False

    while Sorted == False:
        Sorted = True
        a = 0
        while a < L1:
            if x[a + 1].lower() < x[a].lower():
                temp = x[a]
                x[a] = x[a + 1]
                x[a + 1] = temp
                Sorted = False
            a = a + 1

#####     Main     #####

#UTAB is a list of UTA school buildings and some given x/y coordinates
print
UTAB = {"BS" : ["The Bookstore",6.25,1.5],
        "COBA" : ["College of Business",6.0,4.0],
        "NH" : ["Nedderman Hall",4.75,2.0],
        "WH" : ["Woolf Hall",5.0,2.75],
        "SH" : ["Science Hall",4.75,2.75],
        "UH" : ["University Hall",4.75,4.25],
        "LIBR" : ["Library",5.0,4.0],
        "UC" : ["University Center",5.5,2.75],
        "RH" : ["Ransom Hall",5.0,3.0],
        "PKH" : ["Pickard Hall",5.5,4.25],
        "MAC" : ["Maverick Activities Center",3.75,2.5],
        "DH" : ["Davis Hall",4.25,4.25],
        "ERB" : ["Engineering Research Building",5.0,1.75]}

keys = UTAB.keys()
MySort(keys)

for value in keys:
    print ("%s (%s)") % (UTAB[value][0], value)
    
print

CurrentLocation = raw_input("Please tell me where you are: ")
CurrentLocation = CurrentLocation.upper()

while CurrentLocation not in UTAB:
    print "Not valid input, please use correct abbreviations"     ,
    print "listed on top of page."
    CurrentLocation = raw_input("Please tell me where you are: ")
    CurrentLocation = CurrentLocation.upper()

print

Destination = raw_input("Please tell me where you want to go: ")
Destination = Destination.upper()

while Destination not in UTAB or Destination == CurrentLocation:
    print "Not valid input, please use correct abbreviations"     ,
    print "listed on top of page.  And do not enter same as"     ,
    print "CurrentLocation."
    Destination = raw_input("Please tell me where you want to go: ")
    Destination = Destination.upper()

x1 = UTAB[CurrentLocation][1]
y1 = UTAB[CurrentLocation][2]
x2 = UTAB[Destination][1]
y2 = UTAB[Destination][2]

Distance = CalculateDistance(x1,y1,x2,y2)
print ("%.2f units") % (Distance)

