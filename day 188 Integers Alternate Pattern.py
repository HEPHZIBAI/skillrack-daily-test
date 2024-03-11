'''
The program must accept N integers as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= N <= 100

Input Format:
	The first line contains N.
	The second line contains N integers each separated by a space.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		6
		12 45 51 10 63 17
	Output:
		12
		63 17
		45 51 10

Example Input/Output 2:
	Input:
		7
		50 25 18 23 90 75 2
	Output:
		50
		75 2
		25 18 23
		90

Example Input/Output 3: 
	Input:
		12	
		210 241 231 151 186 293 189 100 129 126 283 246
	Output:
		210
		283 246
		241 231 151
		189 100 129 126
		186 293
'''


﻿n=int(input())
l=list(map(int,input().split()))
i=0
while(len(1)>i):
	i+=1
	if i&1:
		print(*l[:i])
		l=l[i:]
	else:
		print(*l[-i:])
		l=1[:-i]
if len(1)!=0: 
	print(*1)
