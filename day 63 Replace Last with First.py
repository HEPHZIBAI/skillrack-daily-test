'''
The program must accept a string S with spaces as the input. For each word W in the string S (i.e., each word from left to right of S), the program must replace th last character of W by the first character of the next word. For the last word, the program must replace the last character by the first character of the first word. Finally, the program must print the modified string S as the output.

Boundary Condition(s): 
	3<= Length of S <= 1000
Input Format: 
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		Nice to meet you
	Output
		Nict tm meey yoN
	Explanation:
		Here S="Nice to meet you".The last character of Nice is replaced by the first character of to. So Nice becomes Nict The last character of to is replaced by the first character of meet. So to becomes tm. The last character of meet is replaced by the first character of you. So meet becomes meey.The last character of you is replaced by the first character of Nice. So you becomes yoN.Hence the output is Nict tm meey yoN

Example Input/Output 2:
	Input:
		tit for tat
	Output
		tif fot tat
'''

a=input().split()
k=0
b=a[0]
c=b[0]
for i in a:
	if k!=0:
		print(i[0], end=" ") 
		print(i[:len(i)-1], end="")
	else:
		print(i[:len(i)-1], end="")
	k+=1
print(c)