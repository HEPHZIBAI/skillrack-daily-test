'''
The program must accept a string S containing only alphabets as the input. The program must print the vowels in the string S alternatively from both ends.

Note: The string S always contains atleast one vowel.

Boundary Condition(s):
	2 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains the vowels in the string S alternatively from both ends.

Example Input/Output 1:
	Input:
		Environment
	Output:
		Eeio
	Explanation:
		The vowels in the string Environment are E, i, o and e.
		So they are printed alternatively from both ends.

Example Input/Output 2:
	Input:
		MANAGERIAL
	Output:
		AAAIE

Example Input/Output 3:
	Input:
		skillrack
	Output: 
		ia
'''
def rt(s):
	vo="aeiouAEIOU"
	vol=[char for char in s if char in vo]
	re=""
	while vol:
		re+=vol.pop(0)
		if vol:
			re+=vol.pop()
	print(re)
	ino=input() 
	rt(ino)
