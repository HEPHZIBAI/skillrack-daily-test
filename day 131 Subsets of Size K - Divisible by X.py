'''
The program must accept three integers N, K and X as the input. The program must print the count of subsets of size K in N which are divisible by X as the output.

Boundary Condition(s):
	1 <= N <= 10^18
	1 <= K <= Total number of digits in N
	1 <= X <= N

Input Format:
	The first line contains N, K and X separated by a space.
	
Output Format:
	The first line contains the count of subsets of size K in N which are divisible by X.

Example Input/Output 1:
	Input:
		2421036 2 6
	Output:
		3
	Explanation:
		The possible subsets of size 2 in 2421036 are 24, 42, 21, 10 and 36.
		Here, the subsets 24, 42 and 36 are divisible by 6.
		Hence the output is 3

Example Input/Output 2:
	Input:
		900456 3 9
	Output: 
		1
'''
a,b,c=input().split()
m=pow(10,int(b))
k=int(b)
l=0
s=0
while(k<=len(a)):
	h=int(a[l:k])
	if h>m//10 and h<m and h%int(c)==0:
		s+=1
	k+=1
print(s) 
