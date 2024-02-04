'''

The program must accept two integers X and Y as the input. The program must form the smallest possible integer N based on the following conditions.
	- The integer N must be formed using all the digits of X. 
	- The value of N must be greater than Y.
Finally, the program must print the value of N as the output. If it is not possible to form such an integer then the program must print -1 as the output.

Boundary Condition(s):
	1 <= X, Y <= 10^7

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first line contains N or -1.

Example Input/Output 1: 
	Input:
		459 500
	Output: 
		549
	Explanation:
		All the possible integers that can be formed using the digits of 459 are459, 495, 549,594, 945 and 954.
		Here 549 is the smallest possible integer which is greater than 500. 
		Hence the output is 549

Example Input/Output 2:
	Input:
		456 660
	Output: 
		-1
'''


import itertools
x,y=map(str,input().strip().split())
y=int(y)
m=-1
l=list(itertools.permutations(x,len(x))) 
l=[int(''.join(i)) for i in 1]
l.sort()
for i in l:
	if i>y:
		print(i)
		break
	else:
		print(-1)