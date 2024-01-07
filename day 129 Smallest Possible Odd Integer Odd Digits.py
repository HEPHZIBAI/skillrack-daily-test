'''
The program must accept a positive integer N as the input. The program must print the smallest possible odd integer S that can be formed with all the odd digits in N as the output. If it is not possible to form such an odd integer, the program must print -1 as the output.

Boundary Condition(s): 
	1 <= N <= 10^8

Input Format: 
	The first line contains N.

Output Format: 
	The first line contains 5 or-1.

Example Input/Output 1: 
	Input: 
		786541
	Output: 
		157
	Explanation:
		The smallest odd integer formed by the odd digits in 786541 is 157. Hence the output is 157

Example Input/Output 2:
	Input: 
		406682
	Output: 
		-1

Example Input/Output 3:
	Input 
		70009
	Output: 
		79
'''


a=int(input())
b=[]
while(a>0):
	m=a%10
	if m%2!=0:
		b.append()
	a//=10
b.sort()

if len(b)==0:
	print("-1")
else
	for i in b:
		print(i, end=")