'''
The program must accept a list of integers as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= Each integer value <= 100

Input Format:
	The first line contains the list of integers.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5 6 1 4 2
	Output:
		*****
		**-**
		**-*-
		**-*-
		**---
		-*---

Example Input/Output 2:
	Input
		7 3 4 5
	Output:
		****
		****
		*-**
		*--*
		*---
		*---
'''

a=list(map(int,input().split())) 
b=max(a)
for i in range(b):
	for j in range(len(a)):
		if(a[d] >0):
			print("*", end="")
		else:
			print('-', end="") 
		a[j]-=1	
	print("\n", end= "")