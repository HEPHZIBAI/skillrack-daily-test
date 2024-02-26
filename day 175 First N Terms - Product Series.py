'''
The program must accept an integer N as the input. The program must print the first N terms in the following series.
The order of series must be 6, 120, 504, 1320 and so on.

Boundary Condition(s):
	1 <= N <= 10^4

Input Format:
	The first line contains N.

Output Format:
	The first line contains the first N terms in the series
separated by a space.

Example Input/Output 1:
	Input:
		2
	Output:
		6 120

Example Input/Output 2:
	Input:
		9
	Output:
		6 120 504 1320 2730 4896 7980 12144 17550
'''


﻿


n=int(input())
s=1
for i in range(n):
	print(s*(s+1)*(s+2), end=" ")
	s+=3
