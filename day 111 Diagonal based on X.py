'''
The program must accept an integer matrix of size NxN and an integer X as the input. The program must print the output based on the following conditions.
-If X is odd, the program must print all the integers along the main diagonal of X. 
- If X is even, the program must print all the integers along the opposite diagonal of X
Note: The integer X has occurred only once in the given NxN matrix.

Boundary Condition(s): 
	2 <= N <= 50

Input Format:
	The first fine contains N.
	The next N lines each contain N integers separated by a space.
	The (N+2)nd line contains X

Output Format:
	The first line contains all the integers along the main diagonal or the opposite diagonal of X


Example Input/Output 1:
	Input:
		4
		77 48 51 82
		13 53 76 68
		64 71 45 53
		87 87 64 24
		45
	Output:
		77 53 45 24
	Explanation:
		The main diagonal of 45 is highlighted below.
		77 48 51 82 
		13 53 76 68
		64 71 45 53
		87 87 64 24

Example Input/Output 2:
	Input:
		5
		41 70 37 49 92
		84 54 46 58 81		
		36 89 53 63 70
		22 13 20 13 59
		35 43 32 28 83
		20
	Output:
		81 63 20 43
	Explanation:
		The opposite diagonal of 20 is highlighted below.		41 70 37 49 92
		84 54 46 58 81		
		36 89 53 63 70
		22 13 20 13 59
		35 43 32 28 83
'''
def ret(l,n):
	a=0;b=0;q=[]
	for i in range(n):
		x=[]; a=0;b=i
		for j in range(i+1):
			x.append(l[a][b])
			a+=1
			b-=1
		q.append(x)
	d=n-1
	for i in range(n-1):
		y=n-1;x=i+1;z=[]
		for j in range(d):
			z.append(l[x][y])
			y-=1
			X+=1
		d-=1
		q.append(z)
	return q

n=int(input())
l=[list(map(int, input().split())) for i in range(n)]
z=int(input())
p=[i[::-1] for i in l]
li=ret(1,n)
pi=ret(p,n)
if z%2==0:
	for i in li:
		if z in i:
			print(*1)
else:
	for i in pi:
		if z in i:
			print(*i)