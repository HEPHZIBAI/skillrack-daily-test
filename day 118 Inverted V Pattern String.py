'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Note: The length of S is always odd.

Boundary Condition(s): 
	3 <= Length of S <= 99

Input Format: 
	The first line contains S.

Output Format: 
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		skill
	Output
		**i**
		*k*l*
		s***l		

Example Input/Output 2:
	Input
		TELEPHONE
	Output
		****P****
		***E*H***
		**L***O**
		*E*****N*
		T*******E
'''

a=input().strip()
k=len(a)//2
u=k
print('*'*k,a[k],'*'*k,sep="")
f=1
x=u-1
y=u+1
k-=1
for i in range(u):
	print('*'*k,a[x], '*'*f,a[y], '*'*k, sep="")
	f+=2
	k-=1
	x-=1
	y+=1