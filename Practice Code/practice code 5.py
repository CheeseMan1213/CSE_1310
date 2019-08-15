
"""
a = 2
if a < 2:
    print a
elif a%2==1 :
    print "nothing"
else:
    print "something"
"""


#any nonzero value is True; Always
#a zero value is False; Always
"""
if 0:
    print "zero is false"
else:
    print "this is always false" #this one will print
"""

#this code will give an opinion of your age
#this is to hel familiarize you with if, else, elif statments
#also on using conditionals such as and, or, not


age = input("Please enter your age:  ")
yes = True
no = False
Yes = True
No = False

if age <= 20:
    print "you are young"
elif 20 < age and age <=40:
    print "you are getting older"
elif age == 50:
    print "did you have your midlife crisis yet?"
    ans = raw_input("Please enter yes or no:  ")
    if ans == True:
        print "sorry"
    elif ans == False:
        print "you will get there"
    elif ans != True or ans != False:
        print "invalid responce"
elif 40 < age and age <=60:
    print "you are old :-)"
elif 60 < age and age <=80:
    print "you are very old :-) :-)"
else:
    print "you are ancient :-("

"""
Bow = 12
bow = 13
print Bow
print bow
"""
