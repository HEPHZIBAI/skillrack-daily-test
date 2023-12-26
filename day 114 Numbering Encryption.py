'''
The program must accept a string S containing only lower case alphabets as the input. The program must replace all the consonants by numbering them from 1 (left to right) in S. Then the program must replace all the vowels by numbering them from 1 (right to left) in S. Finally, the program must print the modified string S as the output.

Boundary Condition(s): 
	1 <= Length of S <= 100

Input Format: 
	The first line contains S.

Output Format: 
	The first line contains the modified string S.

Example Input/Output 1:
	Input
		skillrack
	Output: 
		122345167
	Explanation:
		The string skillrack contains 2 vowels and 7 consonants. The consonants in the string skillrack are numbered from left to right as 12i345a67. The vowels in the string skillrack are numbered from right to left as 12 345 67. Hence the output is 122345167

Example Input/Output 2:
	Input 
		abcdefghijklmnopqrstu
	Output 
		5123445637891011212131415161
'''

a=input().strip()
c=1
for i in a:
	if(i in "aeiouAEIOU"):
		s+=1

for i in a:
	if(i in "aeiouAEIOU"): 
		print(s,end="") 
		s-=1 
	else:
		print(c,end="") 
		c+=1