'''
The program must accept a string S as the input. The program must rotate all the vowels in the string S in the clockwise direction at their positions 1 time. Then the program must print the modified string S as the output.
Note: At least one vowel is always present in the string S.

Boundary Condition(s): 
	1 <= Length of S <= 1000

Input Format: 
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		national
	Output:
		natainol
	Explanation:
		After rotating the vowels in the clockwise direction by 1 time, the string becomes natainol Hence the output is natainol

Example Input/Output 2:
	Input:
		AElou
	Output
		UAElo
'''
a=input().strip()
for i in a:
	if(i in "aeiouAET" ):
		b+=i 
d=len(b) 
b=b[d-1] b[0:d-1] 
k=0
for i in a: 
	if(i in "aeiouAEIOU"): 
		print (b[k], end "")
		k+=1
	else: 
		print(i, end="")