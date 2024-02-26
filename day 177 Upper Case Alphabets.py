'''
The program must accept two string values S1 and S2 containing only alphabets as the input. The program must print yes if all the upper case alphabets (A to Z) present only once in two string values. Else the program must print no as the output.

Boundary Condition(s):
	1 <= Length of S1, S2 <= 100

Input Format:
	The first line contains S1.
	The second line contains S2.

Output Format:
	The first line contains yes or no.

Example Input/Output 1:
	Input
		ABCDEFGHIJKLMNO
		PQRSTUVWXYZ
	Output: 
		yes
	Explanation:
		Here all the upper case alphabets (A to Z) occur only once in two string values.
		So yes is printed.

Example Input/Output 2:
	Input:
		FEDCBA
		GHIJKLMNOPQRSTUVWXYZ
	Output:
		yes

Example Input/Output 3: 
	Input:
		CBADEFGHIjkl
		MNOPQRSTUVWXYZ
	Output:
		no
'''


﻿

s1,s2=input().strip(),input().strip()
s,ct=s1+s2,0
for i in range(65,91): 
	if s.count(chr(i))>1: 
		print("no")
		exit()
	elif s.count(chr(i))==1:
		ct+=1 
if ct==26: 
	print("yes") 
else:
	print("no")

