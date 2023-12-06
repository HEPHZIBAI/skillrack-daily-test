'''
The program must accept an odd integer N as the input. The program must print the desired pattern as shown in Example Input/Output section.

Boundary Condition(s): 
	3 <= N <= 99

Input Format:
	The first line contains N.

Output Format:
	The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
	Output:
		%---%
		---%-
		--%--
		-%---
		%---%

Example Input/Output 2:
	Input:
		7
	Output:
		%-----%
		-----%-
		----%--
		---%---
		--%----
		-%-----
		%-----%
'''


x=int(input())
l=[]
c=0
for k in range(x): 
	for j in range(x): 
		if j==c or j==(c+(x-1)) : 
			print("%", end="") 
		elif k==int(x-1) and j==(x-1): 
			print("%", end="") 
		else: 
			print("-",end="")
	print() 
	c-=1