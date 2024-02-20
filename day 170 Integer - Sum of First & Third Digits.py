'''

The program must accept an integer N as the input. The program must print yes if the sum of the first and third digits is present in N. Else the program must print no as the output.

Boundary Condition(s):
	100 <= N <= 10^8

Input Format:
	The first line contains N.

Output Format:
	The first line contains yes or no.

Example Input/Output 1:
	Input:
		968172
	Output: 
		yes
	Explanation:
		The sum of the first and third digits in 968172 is 17.
		The sum 17 is present in the integer 968172.
		Hence the output is yes

Example Input/Output 2:
	Input:
		747134
	Output:
		no
'''
﻿

a=input().strip()
h=int(a[0])+int(a[2])
h=str(h)
if h in a:
	print("yes")
else:
	print("no")
