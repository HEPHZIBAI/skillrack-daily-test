'''
The program must accept an integer array of size N and an integer K as the input. The program must reverse the alternate sub-arrays of size K in the given array. Then the program must print the N integers in the modified array as the output. If there are no K integers in the last sub-array then reverse the remaining integers in that sub-array.

Boundary Condition(s):
	3 <= N <= 1000
	1 <= Each integer value <= 10^8
	2 <= K <= N

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.
	The third line contains K.

Output Format:
	The first line contains the N modified integers separated by
a space.

Example Input/Output 1:
	Input:
		8
		2 9 8 3 5 3 8 1
		2
	Output:
		9 2 8 3 3 5 8 1
	Explanation:
		Here K = 2.
		After reversing the alternate sub-arrays of size 2 in the array, the integers become 9 2 8 3 3 5 8 1
		Hence the output is 9 2 8 3 3 5 8 1

Example Input/Output 2:
	Input:
		10
		22 23 12 10 34 56 67 13 45 12
		4
	Output:
		10 12 23 22 34 56 67 13 12 45

Example Input/Output 3: 
	Input:
		5
		5 8 7 1 2
		2
	Output: 
		8 5 7 1 2
'''


n=int(input())
a=list(map(int,input().split()))
k=int(input())
i=0
m=1
while(i<len(a)): 
	b=a[i:i+k]
	if m%2!=0:
		for z in b[::-1]:
			print(z, end=" ")
	else:
		for z in b:
			print(z, end=" ")

	i+=k
	m+=1
