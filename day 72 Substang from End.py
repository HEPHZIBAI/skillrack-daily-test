'''
The program must accept a string $ as the input. The programme substring values of 5 in reverse order as the output

Boundary Condition(s)
	2<=Length of 5 <= 100

Input Format:
	The first line contains 5

Output Format
	The first line contains the substring values of Sin reverse order.

Example Input/Output 1:
	Input 
		Brick
	Output
		kckickrickBrick
	Explanation:
		In the string "Brick", the last one character is k. So k is printed 
		The last two characters are c and k. So ck is printed. 
		The last three characters are ic and k. So ick is printed. 
		The last four characters are ric and k. So rick is printed 
		The last five characters are Bric and k. So Brick is printed

Example Input/Output 2:
	Input:
		dolphin
	Output
		ninhinphinlphinolphindolphin

'''
a=input().strip()
for i in range(len(a)):
	b=len(a)-i-1
	d=a[b:]
	print (d, end="").