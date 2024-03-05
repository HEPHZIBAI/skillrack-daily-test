'''
The program must accept N integers as the input. The program must sort the integers in ascending order based on the number of zeros in their binary representation. Then the program must print the N sorted integers as the output. If more than one integers have the same number of zeros in their binary representation, the program must sort those integers in the given order.

Boundary Condition(s):
	2 <= N <= 100
	1 <= Each integer value <= 10^5

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the N modified integers.

Example Input/Output 1:
	Input:
		14 488 64 47
	Output:
		14 47 488 64
	Explanation:
		The binary representation of 14 is 1110 and the number of zeros in it is 1.
		The binary representation of 488 is 111101000 and the number of zeros in it is 4.
		The binary representation of 64 is 1000000 and the
number of zeros in it is 6.
		The binary representation of 47 is 101111 and the number of zero in it is 1.
		So they are sorted based on the number of zeros in their binary representation.

Example Input/Output 2:
	Input:
		5
		4 3 8 7 1
	Output: 
		3 7 1 4 8
'''


n=int(input())
a=list(map(int,input().split()))
g={}
for i in a:
	u=i 
	b=[]
	
	while(u>0):
		b.append(u%2)
		u//=2
	z=0
	if 0 in b:
		z=b.count(0)
	if z not in g:
		g[z]=[i]
	else:
		g[z].append(i)


k=list(g.keys())
k.sort()
for i in k:
	for j in g[i]:
		print(j,end=" ")
