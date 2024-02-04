'''
The program must accept an integer matrix of size RxC and an integer K as the input. The program must print yes if the given RxC matrix contains at least one KXK submatrix with all the integers having the same value. Else the program must print no as the output.

Note: The value of K is always less than R and C.

Boundary Condition(s):
	3 <= R, C <= 502 <= K <= 40

Input Format:
	The first line contains R and C separated by a space.
	The next R lines, each contain C integers separated by a space.
	The (R+2)nd line contains K.

Output Format:
	The first line contains yes or no.

Example Input/Output 1:
	Input:
		5 6
		1 2 3 4 5 5 
		5 2 5 2 4 5 
		6 4 7 5 4 34
		5 7 7 4 5 454
		7 7 7 5 5 100
		2
	Output: 
		yes
	Explanation:
		In the 5x6 matrix, the 2x2 submatrix with all the integers having the same value is highlighted below.
		1 2 3 4 5 5 
		5 2 5 2 4 5 
		6 4 7 5 4 34
		5 7 7 4 5 454
		7 7 7 5 5 100
		Hence the output is yes

Example Input/Output 2:
	Input:
		4 5
		98 98 98 10 71
		53 98 98 91 53
		96 77 80 22 22
		22 28 94 66 34
		3
	Output:
		no
'''


r,c=map(int,input().split())
m=[list(map(int,input().split())) for in range(r)]
k=int(input())
for i in range(r-k+1):
	for j in range(c-k+1):
		s=[x[j:j+k] for x in m[i:i+k]]
		if all(all(y==s[0][0] for y in x) for x in s):
			print("yes") 
			exit()
print("no")