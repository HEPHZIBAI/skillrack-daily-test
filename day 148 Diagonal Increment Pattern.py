'''

The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
3 <= N <= 100

Input Format:
	The first line contains N.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		6
	Output: 
		1 * * * * 2
		* 3 * * 4 *
		* * 5 6 * *
		* * 7 8 * *
		* 9 * * 10 *
		11 * * * * 12

Example Input/Output 2:
	Input:
		5
	Output:
		1 * * * 2
		* 3 * 4 *
		* * 5 * *
		* 6 * 7 *
		8 * * * 9
'''
n=int(input())
a=[]
k=1 
f=n-1
for i in range(n): 
	b=[]
	for j in range(n): 
		if i==j:
			b.append(k)
			k+=1
		elif j==f:
   			b.append(k)
			k+=1
		else:
			b.append("*")
	a.append(b)
	f-=1
for i in a:
	for j in i:
		print(j,end=" ")
	print()
