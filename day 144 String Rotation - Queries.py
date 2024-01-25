'''
The program must accept a string S and Q queries as the input. Each query contains an alphabet D and an integer M. The alphabet D represents a direction (L or R). The integer M represents a magnitude. For each query, the program must modify the string S based on the conditions.
- If the direction is L, then the program must rotate the string S by M positions in the clockwise direction.
- If the direction is R, then the program must rotate the string S by M positions in the anticlockwise direction.
After processing each query, the program must print the first character in the modified string as the output.

Boundary Condition(s):
	1 &lt;= Length of S &lt;= 100
	1 &lt;=Q &lt;= 30
	0 &lt;= M &lt;= 100

Input Format:
	The first line contains S.
	The second line contains Q.
	The next Q lines, each containing D and M separated by a space.

Output Format:
	The first line contains the string as per the given conditions.

Example Input/Output 1:
	Input:
		carriage
		3
		L 3
		R 2
		L 2
	Output:
		rar
	Explanation:
		Here the string is carriage.
		The first query is L 3, so the string carriage is rotated by 3 positions in the clockwise direction. The string becomes riagecar.
		The second query is R 2, so the string riagecar is rotated by 2 positions in the anticlockwise direction. The string becomes arriagec.
		The third query is L 2, so the string arriagec is rotated by 2 positions in the clockwise direction. The string becomes riagecar.
		The accumulated first characters are rar.
		Hence the output is rar

Example Input/Output 2:
	Input:
		enormous
		4
		R 4
		L 1
		R 7
		L 4
	Output:
		mouo
'''


a=input().strip()
n=int(input())
b=""
for i in range(n):
	x,y=input().split()
	y=int(y)
	if x=='L':
		for i in range(y):
			a=a[1:]+a[0]
	else:
		l=len(a)-1
		for i in range(y): 
			a=a[l]+a[:l]
	print(a[0], end="")