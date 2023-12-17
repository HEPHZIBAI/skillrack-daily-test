'''
A boy wants to send a secret code S containing a's and b's to his friend. He designs a method to encrypt the code using two key values X and Y. The technique that he used to encrypt the secret code is given below.
-The integers X and Y represent the numerical value of alphabets a and b respectively (where X I= Y).
- Replace each occurrence of the alphabet a by the integer X.
- Replace each occurrence of the alphabet b by the integer Y.
The program must accept the encrypted string E and two integers X and Y as the input. The program must decrypt the string E and print the original secret code S as the output.

Boundary Condition(s): 
	1 <= Length of E <= 1000 
	0 <=XY <= 10^8

Input Format:
	The first line contains E
	The second line contains X and Y separated by a space.

Output Format: 
	The first line contains S.

Example Input/Output 1:
	Input 
		55665656566 
		5 6
	Output
		aabbabababb
	Explanation:
		After replacing each occurrence of $ in "55665656566" by the alphabet a, the string
		After replacing each occurrence of 6 in "aa66a6a6a66" by the alphabet b, the string becomes aabbabababb.
		Hence the output is aabbabababb

Example Input/Output 2:
	Input:
		875687568787568787
		87 8756
	Output 
		bbabaa
'''

s=input().strip()
x,y=input().split()
i=0
m,n,l=max(len(x),len(y)), min(len(x),len(y)),len(s)
c,s1=0,""

while(i<len(s)):
	if i+m<=l and s[i:i+m]==x or s[i:i+m]==y:
		c+=1
		if s[i:i+m]==x:
			s1+='a'
		else:
			s1+='b'
		i+=m
	elif i+n<=1 and s[i:i+n]==x or s[i:i+n]==y:
		c+=1
		if s[i:i+n]==x:
			s1+='a'
		else:
			s1+='b'
		i+=n
print(s1)