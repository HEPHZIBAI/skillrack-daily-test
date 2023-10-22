'''
The program must accept an odd integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	5 <= N <= 99

Input Format:
	The first line contains N.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
	Output
		1*1
		22*
		3**
		44*
		5*5

Example Input/Output 2:
	Input
		7
	Output
		1**1
		2*2*
		33**
		4***
		55**
		6*6*
		7**7
'''


n = int(input())
x = (n+1)//2
for i in range(1,n+1): 
	for j in range(x):
		if j==0: 
			print(i,end='')
		elif i<x and x-i-j==0: 
			print(i,end=' ')
		elif i>x and x+j==i: 
			print(i,end=' ')
		else: 
			print('*',end=' ')
	print()