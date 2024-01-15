'''
The program must accept a character matrix of size RxC as the input. The program must print all the characters of the given matrix in the ZigZag fashion as shown in the Example Input/Output section.

Boundary Condition(s): 
	2 <= R, C <= 30

Input Format:
	The first line contains R and C separated by a space.
	The next R lines each contain C characters separated by a space.

Output Format:
	The first line contains all the characters in the given matrix.

Example Input/Output 1: 
	Input:
		4 4
		a p p r
		n e h e
		s i v e
		s s e n

	Output: 
		apprehensiveness

Example Input/Output 2:
	Input: 
		3 5
		P e r s o
		c i f i n
		a t i o n

	Output:
		Personification

'''


r,c=map(int, input().strip().split())
ls=[list(map(str, input().strip().split())) for i in range(r)]
row=col=0

while row!=r and col!=c:
	print(ls[row][col], end="")
	col=col + (-1 if row 2 else 1)
	if col==c or col==-1:
		row+=1
		if col==c:col-=1
		else:col+-1