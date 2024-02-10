'''

The program must accept an integer matrix of size RxC as the input. For each column in the matrix, the program must bring all the odd integers to the top of the column in the same order as in the matrix. Finally, the program must print the modified matrix as the output.

Boundary Condition(s):
	2 <= R, C <= 50

Input Format:
	The first line contains R and C separated by a space.
	The next R lines, each containing C integers separated by a space.

Output Format:
	The first R lines, each containing C integers separated by a space.

Example Input/Output 1:
	Input:
		5 4
		22 30 41 33
		89 88 72 57
		17 37 26 63
		52 52 78 75
		80 23 55 69
	Output:
		89 37 41 33
		17 23 55 57
		22 30 72 63
		52 88 26 75
		80 52 78 69
	Explanation:
		The odd integers in the given 5x4 matrix are highlighted below.
		22 30 41 33
		89 88 72 57
		17 37 26 63
		52 52 78 75
		80 23 55 69
		After bringing all the odd integers to the top of the column, the matrix becomes
		89 37 41 33
		17 23 55 57
		22 30 72 63
		52 88 26 75
		80 52 78 69

Example Input/Output 2:
	Input:
		3 4
		80 76 97 71
		82 91 38 15
		14 74 53 49
	Output:
		80 91 97 71
		82 76 53 15
		14 74 38 49

'''


﻿
r,c=map(int,input().split())
a=[]
b=[]
for i in range(r):
	b=list(map(int,input().split()))
	a.append(b)

b=[]
for i in range(c):
	d=[]
	e=[]
	for j in range(r):
		if(a[j][i]%2!=0):
			d.append(a[j][i])
		else:
			e.append(a[j][i])
	b.append(d+e)

for i in range(r):
	for j in range(c):
		print(b[j][i],end=" ")
	print()
