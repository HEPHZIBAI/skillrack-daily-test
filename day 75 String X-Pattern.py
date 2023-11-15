'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s)
	3< Length of S<= 50

Input Format: 
	The first line contains S.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		water
	Output
		w * * * a
		* t * e *
		* * r * *
		* t * e *
		w * * * a

Example Input/Output 2:
	Input
		OFFICE
	Output
		O * * * * F
		* F * * I *
		* * C E * *
		* * C E * *
		* F * * I *
		O * * * * F
'''

s=input().strip() 
n=len(s); 
l= []; 
ans = []
a=0
for i in range(len(s)):
	for j in range(len(s)):
		if (i == j or n-i-1 == j) and a <n: 
			l.append(s[a]) 
			a += 1
		else:
			l.append("*")
		ans.append(l) 
		l = []
if n % 2 == 1:
	for i in ans[:(n//2) + 1]: 
		print(*i)
	for i in ans[:(n//2)][::-1]: 
		print(*i)
else:
	for i in ans[:n//2]: 
		print(*i)
	for i in ans[:n//2][::-1]: 
		print(*i)