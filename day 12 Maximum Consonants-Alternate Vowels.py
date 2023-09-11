'''
The program must accept a string $ as the input. The program must print the maximum number of consonants between the alternate vowels in S as the output. Note: The string 5 always contains atleast two vowels.

Boundary Condition(s):
	3 <= Length of S <= 1000
Input Format: 
	The first line contains S.
Output Format: 
	The first line contains the maximum number of consonants between the alternate vowels.

Example Input/Output 1: 
	Input
		skillrackCODINGPLATFORM
	Output
		4
	Explanation:
		The number of consonants between the vowels T and 'a' in the string ski ackCODINGPLATFORM is 3.
		The number of consonants between the vowels 'a' and 'O' in the string skilla CODINGPLATFORM is 3. 
		The number of consonants between the vowels 'O' and 'T' in the string skillrackCO INGPLATFORM is 1.
		The number of consonants between the vowels 'T' and 'A' in the string skillrackCODIATFORM is 4.
		The number of consonants between the vowels 'A' and 'O' in the string skillrackCODINGPLA ORM is 2.
		Here the maximum number of consonants is 4.
		Hence the output is 4

Example Input/Output 2:
	Input
		aaao
	Output
		0
'''
s=input().strip()
m=0
for i in range(len(s)-1): 
	for j in range(i+1, len(s)): 
		if s[i] in 'aeiouAEIOU and s[j] in 'AEIOUaeiou':
			m=max(m, (j-i-1))
			break
print(m)


