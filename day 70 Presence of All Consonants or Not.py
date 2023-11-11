'''
The program must accept a string S containing only lower case alphabets as the input. The program must print YES if all the consonants are present in the string S (in any order). Else the program must print NO as the output.

Boundary Condition(s):
	26<=Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains either YES or NO.

Example Input/Output 1:
	Input:
		abcdefghijklmnopqrstuvwyz
	Output: 
		YES
	Explanation:
		All the 21 consonants (bcdfghjklmnpqrstvwxyz) are present in the string abcdefghimnopqrstuvwxyz. So YES is printed.

Example Input/Output 2:
	Input
		pabchirgstwklmndfhjbcgstmms
	Output
		NO
'''

a=input().strip()
b="bcdfghjklmnpqrstvwxyz"
i=0
while(i<len(b) and b[i] in a):
	i+=1
	if(i==21):
		print("YES")
	else:
		print("NO")