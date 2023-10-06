'''
The program must accept a string M containing three upper case alphabets as the input. M represents a month in a non-leap year. The program must print the calendar of the month M where the starting day of the month is always SUNDAY as shown in the Example Input/Output section. The order of weekdays in the calendar is given below. 

1-SUN
2-MON 
3-TUE
4-WED
5-THU
6-FRI
7-SAT

Input Format: 
	The first line contains M.

Output Format:
	The lines containing the calender of the month M as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		AUG
	Output
		01 02 03 04 05 06 07
		08 09 10 11 12 13 14
		15 16 17 18 19 20 21 
		22 23 24 25 26 27 28
		29 30 31 -- -- -- --

Example Input/Output 2:
	Input: 
		FEB
	Output
		01 02 03 04 05 06 07
		08 09 10 11 12 13 14
		15 16 17 18 19 20 21 
		22 23 24 25 26 27 28
'''

a=input().strip()
m=0
if(a=="JAN" or a=="MAR" or a=="MAY"  or a=="JUL" or a=="AUG" or a=="OCT" or a=="DEC"):
	m=31
elif("FEB"): 
	m=28
else:
	m=30
k=1
while(k<=m):
	for i in range(7):
		if(k<10):
			print('0',end="")
			print(k, end") 
		elif(k<=m):
			print (k, end"")
		else:
			print ("--", end" ")
		k+=1
	print("\n", end="")
