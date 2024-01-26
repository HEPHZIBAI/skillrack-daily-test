'''
The program must accept N integers as the input. The program must sort all the integers in descending order based on their factors count. If more than one integer has the same factors count then the program must sort those integers based on their order of occurrence. Finally, the program must print the sorted integers as the output.

Boundary Condition(s):
	2 <= N <= 1000
	1 <= Each integer value <= 10^5

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains N sorted integers separated by a space.

Example Input/Output 1:
	Input:
		3
		121 100 24
	Output:
		100 24 121
	Explanation:
		The factors of 121 are 1, 11 and 121. So the factors count of 121 is 3.
		The factors of 100 are 1, 2, 4, 5, 10, 20, 25, 50 and 100. So the factors count of 100 is 9.
		The factors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. So the factors count of 24 is 8.
		So the integers are sorted based on their factors count and printed as the output.

Example Input/Output 2:
	Input:
		7
		5 11 10 20 9 16 23
	Output:
'''


n=int(input())
a=list(map(int,input().split()))
b={}
for i in a:
	s=0
	for j in range(1,i): 
		if(i%j==0):
			s+=1
	if s not in b:
		b[s]=[i]
	else:
		b[s].append(i)

f=list(b.keys())
f.sort()
for i in f[::-1]:
	for j in b[i]:
