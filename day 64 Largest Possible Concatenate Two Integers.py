'''
The program must accept three integers X, Y and Z as the input. The program must print the largest possible integer which is obtained by concatenating any two integers among X, Y and Z as the output.

Boundary Condition(s): 
	0 <= X Y, Z <= 10^5

Input Format: 
	The first line contains X, Y and Z.

Output Format
	The first line contains an integer based on the given condition.

Example Input/Output 1:
	Input: 
		100 2 10
	Output 
		10100
	Explanation
		The largest possible integer 10100 is obtained by concatenating the integers 10 and 100.Hence the output is 10100

Example Input/Output 2:
	Input 
		45 81 12
	Output 
		8145

Example Input/Output 3:
	Input
		0 2 5
	Output
		52
'''
a=list(map(int, input().split())) 
a.sort(reverse=True)
x=int(str(a[0])+str(a[1]))
y=int(str(a[1])+str(a[0]))
if x>y:
	print(x)
else:
	print(y)