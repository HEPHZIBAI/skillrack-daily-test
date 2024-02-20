'''
The program must accept a string S as the input. The program must print the ASCII values of all the characters in the string S as shown in the Example Input/Output section.

Boundary Condition(s):
	2 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		mark
	Output:
		********109
		******97***
		***114*****
		107********

Example Input/Output 2:
	Input:
		SkillRack
	Output:
	*********************83
	******************107**
	***************105*****
	************108********
	*********108***********
	*******82**************
	*****97****************
	***99******************
'''


﻿

a=input().strip()
s=0

for i in a:
	x=ord(i)
	y=str(x)
	s+=len(y)
t=s

for i in a:
	x=str(ord(i))
	y=s-len(x)
	for j in range(y):
		print("*", end="")
	print(ord(i),end="") 
	for i in range(s,t):
		print("*",end="")
	print()
