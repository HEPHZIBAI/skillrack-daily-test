'''
The program must accept two integers X and Y as the input. The program must print the count of common digits in X and Y as the output.

Boundary Condition(s): 
	1 <=X,Y <= 10^8

Input Format:
	The first line contains X The second line contains Y.

Output Format:
	The first line contains the count of common digits in X and Y.

Example Input/Output 1:
	Input
		5436
		65547
	Output
		3
	Explanation
		The common digits in 5436 and 65547 are 5, 4 and 6. Hence the output is 3

Example Input/Output 2:
	Input:
		22
		22222
	Output
		2
'''

a=input().strip()
b=input().strip()
c=a+b
c=set(c)
c=list(c)
k=""
for i in c:
	if(i in b and i in a):
		x=a.count(i)
		y=b.count(i)
		if(x<=y):
			h=i*x
			k+=h
		else:
			h=i*y
			k+=h
print(len(k))