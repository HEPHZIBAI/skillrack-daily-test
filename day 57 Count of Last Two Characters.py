'''
The program must accept a string S as the input. The program must find and print the number of occurrences of the last two characters of 5 in the same string 5 as the output.

Boundary Condition(s): 
	2 <= Length of S <= 10^4

Input Format: 
	The first line contains S.

Output Format:
	The first line contains the number of occurrences of the last two characters of 5 in the same string S.

Example Input/Output 1: 
	Input
		hiabchi
	Output 
		2
	Explanation:
		The last two characters of the string hiebehi are h and L. Here the hi has occurred 2 times in the string hiabchi.Hence the output is 2

Example Input/Output 2:
	Input:
		MOOONOO
	Output
		3
'''

a=input().strip()
b=a[-2]+a[-1]
s=0
i=0
while(i<len(a)-1):
	if(a[i]==a[-2] and a[i+1]==a[-1]):
		s+=1	
	i+=1
print(s)