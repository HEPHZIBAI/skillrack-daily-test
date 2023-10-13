'''
The program must accept an integer N and a list of integers representing the factors of N as the input. At least one factor of N is always missing the given list of integers. The program must find and print those missing factors of N in ascending order as the output.

Boundary Condition(s):
	2 <= N <= 10^8

Input Format:
	The first line contains N.
	The second line contains a list of integers representing the factors of N separated by a space

Output Format:
	The first line contains the missing factors of N in ascending order separated by a space.

Example Input/Output 1:
	Input 
		100
		2 100 1 10 50
	Output
		4 5 20 25
	Explanation:
		The factors of 100 are 1 2 100 50 and 100. The missing factors are printed in ascending order 45 20 25 Hence the output is 4 5 20 25

Example Input/Output 2:
	Input 
		4
		1 4
	Output
		2
'''

n=int(input())
b=list(map(int, input().split())) 
for i in range(1,n+1):
	if(n%i==0):
		if(i not in b): 
			print(i, end=" ")