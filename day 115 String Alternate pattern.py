'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	1 <= Length of S <= 100

Input Format: 
	The first line contains S.

Output Format: 
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		abcdefghijklmno
	Output
		a
		no
		bcd
		jldm
		efghi

Example Input/Output 2:
	Input:
		skillrack
	Output:
		S
		ck
		kil
		Ira

Example Input/Output 3:
	Input
		junk
	Output
		j
		nk
		u
'''

n=input().strip()
ct=1
while n:
	if ct&1:
		print(n[:ct])
		n=n[ct:]
	else:
		print(n[-ct:])
		n=n[:-ct]
	ct+=1