'''
The program must accept an integer matrix of size NxN as the input. The program must print YES if the matrix has at least one repeated 2x2 submatrix without overlapping. Else the program must print NO as the output.

Boundary Condition(s):
	4 <= N <= 25

Input Format:
	The first line contains N.
	The next N lines each contain N integers separated by a space.

Output Format:
	The first line contains either YES or NO.

Example Input/Output 1:
	Input:
		4
		4 5 7 8
		6 2 1 6
		1 2 4 5
		9 4 6 2
	Output: 
		YES
	Explanation:
		The repeated 2x2 submatrices without overlapping are highlighted below.
		4 5 7 8
		6 2 1 6
		1 2 4 5
		9 4 6 2

Example Input/Output 2:
	Input:
		6
		28 44 22 23 44 41
		14 40 20 33 10 12
		16 29 10 20 33 33
		49 49 49 10 20 25
		49 49 49 32 45 33
	Output:
		NO
'''
n=int(input())
1st-[]
for _ in range(n):
	1st.append(list(map(int, input().split())))

def isValid(visit vals):
	for r in range(n-1):
		for c in range(n-1):
			if (r, c) in visit or (r+1,c) in visit or (r+1,c+1) in visit or (r, c+1) in visit: 
				continue
			if 1st[r][c]==vals[0] and lst[r][c+1]==vals[1] and 1st[r+1][c]==vals[2] and lst[r+1][c+1]==vals[3]:
				return True
	return False


def func():
	for i in range(n-1):
		for j in range(n-1): 
			vals =[1st[i][j], 1st[i][j+1], 1st[i + 1][j], lst[i + 1][j + 1]] 
			visit = set([(i, j), (i + 1, j), (i,j+1), (i + 1, j + 1)])
			
			if isValid(visit, vals):
				return "YES"
	return "NO" 
print(func())


