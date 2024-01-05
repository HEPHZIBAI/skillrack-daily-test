'''
The program must accept two integers X and Y as the input. The program must choose exactly one digit from the digits of X and exactly one digit from the digits of Y. The program must form the largest possible two-digit odd integer T from the choosen digits. If it is not possible to form T, the program must print -1 as the output.

Boundary Condition(s): 
	10 <=X, Y <= 10^8

Input Format:
	The first line contains X and Y separated by a space.

Output Format: 
	The first line contains the largest possible two-digit odd integer or -1.

Example Input/Output 1:
	Input 
		1684 3457
	Output 
		87
	Explanation:
		All possible two-digit odd integers are 13, 15, 17, 63, 65, 67, 83, 85, 87, 43, 45, 47, 31, 41, 51 and 71.
		Here the largest possible two-digit odd integer is 87. Hence the output is 87

Example Input/Output 2:
	Input: 
		48 802
	Output: 
		-1

Example Input/Output 3:
	Input
		9088 296
	Output: 
		99
'''

a,b=input().split()
l=0
f=1

for i in a:
	for j in b:
		k=i+j
		k=int(k)
		h=j+i
		h=int(h)
		if(k%2!=0 and l<k):
			l=k
			f=0
		if(h%2!=0 and l<h):
			l=h
			f=0
if f:
	print("-1")
else:
	print(l)