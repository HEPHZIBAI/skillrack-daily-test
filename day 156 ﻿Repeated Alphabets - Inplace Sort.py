'''
The program must accept a string S containing lower case alphabets as the input. The program must sort the repeated alphabets in S in their positions. Then the program must print the modified string S as the output.

Boundary Condition(s):
	2 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		skillrack
	Output: 
		skiklracl
	Explanation:
		The repeated alphabets in the string "skillrack" are highlighted below skillrack
		After sorting the repeated alphabets in their positions, the string becomes "skiklracl"
		So skiklracl is printed as the output.

Example Input/ Output 2:
	Input:
		abcbgbchcbftflkf
	Output:
		abbbgbchccftflkf

Example Input/Output 3:
	Input:
		tattarrattat
	Output:
		aaaarrtttttt
'''

a=input().strip()
b=""
for i in a:
	if a.count(i)>1:
		b+=i
b=list(b)
b.sort()
C=""
k=0
for i in a:
	if i not in b:
		c+=i
	else:
		c+=b[k] 
		k+=1
print(c)