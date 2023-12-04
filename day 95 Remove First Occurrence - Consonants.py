'''
The program must accept a string S as the input. The program must remove the first occurrence of all the repeated consonants in the string S. Then the program must print the modified string S as the output.

Boundary Condition(s):
	3 <= Length of S <= 1000

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input
		Attendance
	Output
		Atedance
	Explanation:
		The repeated consonants in the string Attendance are t and n. So the first occurrence of both the consonants are removed from the string Attendance.Hence the output is Atedance

Example Input/Output 2:
	Input:
		Cloud
	Output:
		Cloud

Example Input/Output 3:
	Input:
		OCcurrence@123
	Output:
		OCurence@123
'''

def isvowel(c):
	c = c.lower()
		return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' 

s = list(map(str, input().strip())); 1 = []
for i in s:
	if i not in l and (not isvowel(i)) and (s.count(i) > 1): 		l.append(i)
	else: 
		print(i, end = "")