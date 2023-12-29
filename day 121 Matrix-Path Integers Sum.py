'''
The program must accept an integer matrix of size RxC and a string P representing a path inside the matrix as the input. The string P contains the alphabets N, E, W and S. The path P always starts from the top-left position of the matrix (i.e., the first row and first column of the matrix). The program must print the sum of integers T which are present in the path P as the output. If the path P crosses a position in the matrix more than once then the integer X which is present in that position will not be added again to the sum T (i.e., Even if the position of X has crossed multiple times by the path P, the integer X is added only once to the sum T).

The path movements are given below.
N-Move one position towards North.
E-Move one position towards East
W-Move one position towards West.
S-Move one position towards South.

Boundary Condition(s):
	2 <= R, C <= 50 
	1 <= Length of P <= 500

Input Format:
	The first line contains R and C separated by a space.
	The next R lines each contain C integers separated by a space. 	The (R+ 2ynd line contains P.

Output Format:
	The first line contains the sum of integers T as per the given condition(s).

Example Input/Output 1:
	Input:
		3 3
		1 2 3
		4 5 6
		7 8 9
		ESENWSSW
	Output
		32
	Explanation:
		The integers which are present in the path ESENWSSW are 125632587. 
		Here the path P crossed the integers 2 and 5 twice. So they are not considered again to find the sum T.
		Hence the sum 32 (1+2+5+6+3+8+7) is printed as the output.

Example Input/Output 2:
	Input:
		4 5
		26 94 92 15 31
		74 67 52 56 39
		92 68 16 31 9
		21 29 79 39 10
		SENESEESWNN
	Output:
		555
'''

r,c=map(int, input().split())
a=[]
x=0
y=0
s=0
b=[]
c=[]

for i in range(r):
	q=list(map(int, input().split()))
	a.append(q)

p=input().strip() 
c.append(a[x][y])
s+=a[x][y]
h=[x,y]
b.append(h)

for i in p:
	if i=='N':
		x-=1
	elif(i=='E'):
		y+=1
	elif(i=='W'):
		y-=1
	elif(i=='S'):
		x+=1

	h=[x,y]
	if h not in b:
		b.append(h) 
		s+=a[x][y]
		c.append(a[x][y])
print(s)
