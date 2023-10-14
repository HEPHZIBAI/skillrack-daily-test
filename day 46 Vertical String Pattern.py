'''
The program must accept N string values as the input. The program must print those N string values vertically as shown in the Example Input/Output section.

Boundary Condition(s):
	1< N, Length of each string <= 100

Input Format:
	The first line contains N. The second line contains N string values separated by a space.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		3
		All is well
	Output:
		Aiw
		Ise
		l*l
		**l

Example Input/Output 2:
	Input:
		4 
		Robotic process automation RPA
	Output:
		RpaR
		oruP 
		botA
		OCO*
		tem*
		isa*
		cst*
		**i*
		**o*
		**n*
'''

n=int(input()) 
a=input().strip() 
a=a.split()
l=0
for i in a: 
	if(len(i)>l):
		l=len(1)
for i in range(l):
	for k in a:
		if(i<len(k)): 
			print(k[i], end="") 
		else:
			print("*", end="")
	print()