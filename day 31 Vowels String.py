'''
The program must accept a string $ containing only alphabets as the input. The program must print YES if all the alphabets in the string S are vowels. Else the program must print NO as the output.

Boundary Condition(s): 
	1 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input
		SkillRack
	Output:
		NO
	Explanation: 
		In the string SkillRack, consonants have occurred. So NO is printed as the output

Example Input/Output 2:
	Input
		AceioO
	Output: 
		YES
'''

a=input().strip()
m=1
for i in a: 
	if i not in ("aeiouAEIOU"):
		m=0
		break
if m:
	print("YES")
else: 
	print("No")