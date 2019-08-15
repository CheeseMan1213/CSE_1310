"""
This program will list the factors of the number you give it.
"""

num = 1
num2 = input("Enter a number:  ")

while 1 <= num and num <= num2:
	if num2%num == 0: 
		print num
	num = num + 1
