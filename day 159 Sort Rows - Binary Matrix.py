'''
The program must accept an integer matrix containing only 1's and O's as the input. The program must sort the rows of the matrix based on the decimal equivalent of each row. Then the program must print the modified matrix as the output.

Boundary Condition(s):
	2 <= R, C <= 25

Input Format:
	The first line contains R and C separated by a space.
	The next R lines, each contain C integers separated by a space.

Output Format:
	The first R lines, each contain C integers separated by a space.

Example Input/Output 1:
	Input:
		5 3
		1 1 1
		0 1 0
		0 1 0
		1 0 0
		0 1 1
	Output:
		0 1 0
		0 1 0
		0 1 1
		1 0 0
		1 1 1
	Explanation:
		The decimal equivalent of the 1st row (1 1 1) is 7. 		The decimal equivalent of the 2nd row (0 1 0) is 2. 		The decimal equivalent of the 3rd row (0 1 0) is 2. 		The decimal equivalent of the 4th row (1 0 0) is 4.
		The decimal equivalent of the 5th row (0 1 1) is 3.
		After sorting the rows based on their decimal equivalent, the matrix becomes
		0 1 0
		0 1 0
		0 1 1
		1 0 0
		1 1 1

Example Input/Output 2:
	Input:
		2 5
		1 0 1 0 1
		0 0 1 1 1 
	Output: 
		0 0 1 1 1
		1 0 1 0 1
'''

r,c=map(int,input().split())
a=[]
3
c={}
for i in range(r):
	b=list(map(int,input().split()))
	a.append(b)

for i in a:
	h=1
	s=0
	for j in i[::-1]: 
		s+=(h*j)
		h*=2
	if s not in c:
		c[s]=[i]
	else:
		c[s].append(i)
d=list(c.keys())
d.sort()

for i in d:
	for j in c[i]:
		for k in j:
			print(k,end=" ")
		print()
