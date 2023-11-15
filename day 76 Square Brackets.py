'''
The program must accept a string S with spaces as the input. The program must convert all the alphabets between each pair of square brackets [] to upper case alphabets. Finally, the program must print the modified string S as the output.

Boundary Condition(s): 
	3 Length of S <= 1000

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input
		uhuu [ntu e]tuhnt[uheo
	Output
		uhuu [NTU E]tuhnt[uheo
	Explanation:
		In the string uhuu [ntu ejtuhnt[uheo, the alphabets within the pair of square brackets are n t u e.After coverting those alphabets into uppercase the string becomes uhuu (NTU Eltuhnt(uheo.
Hence the output is uhuu [NTU Etuhnt(uheo

Example Input/Output 2:
	Input
		[robert [was] a good [king]
	Output:
		[robert [WAS] a good [KING]

Example Input/Output 3:
	Input
		[as[df]er]
	Output 
		[as[DF]er]
'''
s=input().strip()
re=""
is_up=False
for i in range(len(s)):
	if s[i]=="[":
		re+=s[i] 
		for z in range(i+1, len(s)):
			if s[z]=="[":
				break
			elif s[2]"]":
				is_up=True
				break
	elif s[i]=="]":
		re+="]"
		is_up=False
	elif is_up:
		re+=s[i].upper()
	else:
		re+=s[i]
print(re)