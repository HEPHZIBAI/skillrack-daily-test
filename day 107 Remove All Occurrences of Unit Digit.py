'''
The program must accept an integer N as the input. The program must remove all the occurrences of N's unit digit in the same integer N. Then the program must print the modified integer N as the output. If all the digits of N are the same, the program must print -1 as the output.

Boundary Condition(s): 
	1 <= N <= 10^18
Input Format: 
	The first line contains N
Output Format: 
	The first line contains the modified integer N or -1.

Example Input/Output 1: 
	Input
		121671
	Output 
		267
	Explanation:
		The unit digit of 121671 is 1. So all the occurrences of 1 are removed from the integer 121671.
		So the modified integer is 267

Example Input/Output 2:
	Input: 
		800180708
	Output
		1070

Example Input/Output 3:
	Input:
		333
	Output
		-1
'''
a=input().strip()
h=a[0]
b=''
for i in a:
	if(i!=a[0]):
		b+=i
if(b!=''):
	print(int(b))
else:
	print(-1)
