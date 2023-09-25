'''
The program must accept two string values $1 and S2 with spaces as the input. The program must align the characters in the vertically down side and then print them as shown in the Example Input/Output section. Note: After aligning both string values, all the white space characters must be replaced by hyphens.

Boundary Condition(s):
	2 <= Length of S1, S2 <= 1000

Input Format:
	The first line contains $1.
	The second line contains S2.

Output Format:
	The first line contains the modified S1. The second line contains the modified $2.

Example Input/Output 1:
	Input
		hello world
		i am very happy
	Output
		h-ll--wor-d----
		leamovery happy

Example Input/Output 2:
	Input:
		this is long text
		its not long
	Output:
		thi--is-long-----
		itssnot-long-text
'''



a=input().strip() 
b=input().strip()
X, y="","" 
m,n=len(a), len(b)
for i in range(min(n,m)): 
	if b[i]==' ':
		if a[i]==' ': 
			y+='-'
		else:
			y+=a[i]
		X+='-'
	else:
		y+=b[i]
		if a[i]==' ':
			x+='-'
		else:
			x+=a[i]
if m>n:
	x+='-'*(m-n)
	y+=a[-(m-n):].replace('','-')
elif m<n: 
	x+='-'* (n-m)
	y+=b[-(n-m):].replace('','-')
print(x)
print(y)