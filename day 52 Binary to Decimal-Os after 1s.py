'''
The program must accept N integers containing only Os and 1s as the input. The program must form a binary representation B by concatenating all the 1s followed by all the Os. Finally, the program must print the decimal equivalent of 8 as the output.

Boundary Condition(s)
	2 < N < 63

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format
	The first line contains the decimal equivalent of B.

Example Input/Output 1
	Input 
		4	
		1 0 0 1
	Output:
		12
	Explanation:
		The binary representation 8 is 1100 formed by concatenating two 1s followed by two The decimal equivalent of 1100 is 12.Hence the output is 12

Example Input/Output 2:
	Input
		6
		0 0 1 1 1 1
	Output:
		60
'''
a=int(input())
b=list(map(int,input().split()))
c=b.count(1)
d=b.count(0)
f=1
s=0
while(d>e):
	f*=2
	d-=1

while(c>0):
	c-=1
	s+=f
	f*=2
print(s)
