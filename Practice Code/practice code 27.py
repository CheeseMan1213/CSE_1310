"""
practice using I/O (input/output) in python

"""


file1 = open("PyInputOutputTest.txt", "r")#  reads existing file
file2 = open("PyInputOutputTest2.txt", "a")# creates new file if does not exist.  Overwrites file if does exist
mysum = 0
for line in file1:
    mysum = mysum + int(line)
file2.write(str(mysum))
file2.write("\n")

file1.close()
file2.close()
