'''
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example input/Output section.
Note: All the digits in N are non-zero digits.

Boundary Condition(s): 
	11 <= N < 10^4

Input Format:
	The first line contains N..

Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input 
		651
	Output
		51 51 51 51 51 51
		61 61 61 61 61
		65

Example Input/Output 2:
	Input
		9845
	Output
		845 845 845 845 845 845 845 845 845
		945 945 945 945 945 945 945 945
		985 985 985 985
		984 984 984 984 984
'''

a=input().strip()
for i in range(len(a)):
	h=int(a[i])
	C=""
	if(i==0):
		c=a[i+1:]+"
	else:
		c=a[i]+a[i+1:]+" "
	print(c*h)