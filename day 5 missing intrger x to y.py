'''
There is a sequence of integers containing the integers from X to Y. The program must accept N integers from the sequence (where X and Y are always present) as the input. The program must print the number of missing integers in the sequence as the output.

Note: N is always less than or equal to total number of integers from X to Y.

Boundary Condition(s)
	2 <= N <= 10^4
	1 <= Each integer value <= 10^5

Input Format:
	The first line contains N. The second line contains N integers separated by a space.

Output Format:
	The first line contains the number of missing integers.

Example Input/Output 1:
	Input 
		5
		4 5 6 10 11
	Output 
		3
	
	Explanation:
		Here the sequence of integers containing the integers from 4 to 11 is 456789 10

Example Input/Output 1:
	Input 
		5
		7 5 6 4 8
	Output 
		0
'''

a=int(input())

b=list(map(int, input().split()))

s=min(b)

l=max(b)

print (abs (l-s-a+1))


