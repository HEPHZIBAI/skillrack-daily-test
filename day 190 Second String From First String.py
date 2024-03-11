'''

The program must accept two string values S1 and S2 are
of equal length as the input. The program must print yes if the second string is formed using all the alphabets in the first string by ignoring the case of alphabets. Else the program must print no as the output.

Boundary Condition(s):
	1 <= Length of S1, S2 <= 1000

Input Format:
	The first line contains S1.
	The second line contains S2.

Output Format:
	The first line contains yes or no.

Example Input/Output 1:
	Input:
		Flow
		Wolf
	Output:﻿
		yes
	Explanation:
		Here the string Wolf is formed using all the alphabets in the string Flow by ignoring the case of alphabets.
		So yes is printed as the output.

Example Input/Output 2:
	Input:
		clOud
		robOt
	Output:
		no
'''

a=input().strip()
b=input().strip()
a=a.lower() 
b=b.lower()
m=1
for i in a:
	if i not in b:
		m=0 
		break
	else:
		if a.count(i)>b.count(i):
			m=0 
			break	
if m==1:
	print("yes")
else:
	print("no")
