'''﻿
The program must accept two integers N and K as the input. The program must print the smallest possible integer by replacing exactly K digits in N with 0.

Boundary Condition(s):
	1 <= N <= 10^8
	1 <= K <= Number of digits in N

Input Format:
	The first line contains N and K separated by a space.

Output Format:
	The first line contains the smallest possible integer by replacing exactly K digits in N with 0.

Example Input/Output 1:
	Input:
		2001356 2
	Output:
		356
	Explanation:
		Here N = 2001356 and K = 2.
		After replacing the two digits 2 and 1 with 0 in 2001356,
		the integer becomes 356 (0000356 = 356).
		Hence the output is 356

Example Input/Output 2:
	Input:
		92 2
	Output: 
		0
'''


a,b=map(int,input().split())
x=str(a)

for i in range(len(x)):
	if x[i]!='0':
		x=x[i]+'0'+x[i+1:]
		b-=1
	if b<=0:
		break
print(int(x)) 