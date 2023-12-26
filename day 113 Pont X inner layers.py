'''
The program must accept an integer matrix of size NxN and an integer X as the input. The program must print the X inner layers of the matrix as the output.

Boundary Condition(s):
	1 < X < N <= 50 
	1<=Each integer value <= 10^5

Input Format:
	The first line contains N. 
	The next N lines each contain N integers separated by a space. 	The (N+2)nd line contains X.

Output Format
	The lines contains the X inner layers of the given matrix.

Example Input/Output 1
	Input:
		7
		8 7 6 5 4 9 2
		1 2 3 4 5 6 7
		9 3 8 2 8 1 6
		1 7 4 8 2 6 9
		5 1 7 2 8 3 4
		6 5 7 3 8 1 2
		7 6 9 2 3 1 8
		2
	Output:
		8 2 8
		4 8 2
		7 2 8
	Explanation: 
		In the given 7x7 matrix, the two inner layers are highlighted below.
		8 7 6 5 4 9 2
		1 2 3 4 5 6 7
		9 3 8 2 8 1 6
		1 7 4 8 2 6 9
		5 1 7 2 8 3 4
		6 5 7 3 8 1 2
		7 6 9 2 3 1 8
		So the two inner layers are printed as the output.

Example Input/Output 2:
	Input:
		8
		12 34 56 78 90 98 76 65
		54 67 89 10 34 26 78 90
		43 56 87 23 22 66 88 78
		23 45 67 87 43 32 66 99
		21 32 43 54 65 76 87 98
		10 29 38 48 57 94 93 52
		78 34 12 54 65 76 23 65
		64 66 33 44 88 98 22 54
		3
	Output
		67 89 10 34 26 78
		56 87 23 22 66 88	
		45 67 87 43 32 66
		32 43 54 65 76 87
		29 38 48 57 94 93
		34 12 54 65 76 23
'''

n = int(input())
lis=[input().split() for i in range(n)] 
x = int(input()) * 2
x=x-1 if n&1 else x
st=(n-x)//2
for i in range(st, st+x):
	print(*lis[i][st: st+x])