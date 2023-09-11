'''
The program must accept a string S containing only lower case alphabets as the input. The program must print YES if the string S is a palindrome after removing any one alphabet from it. Else the program must print NO as the output.

Boundary Condition(s):
	2 <= Length of S <= 100

Input Format: 
	The first line contains S.

Output Format: 
	The first line contains YES or NO.

Example Input/Output 1: 
	Input
		abkcddcba
	Output 
		YES
	Explanation:
		After removing the alphabet from ab cddcba, the string becomes abcddcba which is a palindrome.Hence the output is YES

Example Input/Output 2:
	Input:
		madam
	Output: 
		YES
Example Input/Output 3:
	Input
		abcdfdeba
	Output: 
		NO
'''



a=input().strip()
f=0
for i in range(len(a)): 
	b=a[0:i]+a[i+1:].strip()
	c=b[::-1].strip()
	if(b==c):
		f=1
		break
if(f):
	print("YES")
else: 
	print("NO")