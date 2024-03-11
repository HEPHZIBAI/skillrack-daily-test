'''
The program must accept an integer matrix of size NxN and an integer K as the input. The program must surround each integer in the matrix with K and print the matrix as shown in the Example Input/Output section.

Boundary Condition(s):
	2 <= N <= 25
	0 <= Each integer value <= 1000

Input Format:
	The first line contains N.
	The next N lines, each containing N integers separated by
a space.
	The (N+2)nd line contains K.

Output Format:
	The lines containing the desired pattern as shown in the
Example Input/Output section.

Example Input/Output 1:
	Input:
		3
		1 2 3
		4 5 6
		7 8 9
		0
	Output:
		0 0 0 0 0 0 0 
		0 1 0 2 0 3 0 
		0 0 0 0 0 0 0 
		0 4 0 5 0 6 0
		0 0 0 0 0 0 0 
		0 7 0 8 0 9 0
		0 0 0 0 0 0 0

Example Input/Output 2:
	Input:
		2
		10 20
		55 30
		99
	Output:
		99 99 99 99 99
		99 10 99 20 99
		99 99 99 99 99
		99 55 99 30 99
		99 99 99 99 99
'''

n=int(input())
a=[]
for i in range(n):
	b=list(map(int,input().split()))
	a.append(b)
k=int(input())
out=[]
b=[k for i in range(n+n+1)]
out.append(b)

for i in a:
	c=[]
	for j in i:
		c.append(k)
		c.append(j)
	c.append(k)
	out.append(c)
	out.append([k for i in range(n+n+1)]

for i in out:
	for j in i:
		print(j,end=" ")
	print()
