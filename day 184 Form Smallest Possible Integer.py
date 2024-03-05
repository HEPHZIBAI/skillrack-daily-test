'''
The program must accept a string S containing only digits as the input. The program must form the smallest possible integer X using the digits in S. Finally, the program must print the value of X as the output.

Boundary Condition(s):
	1 <= Length of S <= 1000

Input Format:
	The first line contains S.

Output Format:
	The first line contains X.

Example Input/Output 1:
	Input:
		5413045415601160561561060606606067888799932266544445
	Output:
		1000000000111111122223344444444445555555555666666666
	Explanation:
		The smallest possible integer formed using the digits in 5413045415601160561561060606606067888799932266544 is 1000000000111111122223344444444445555555555666666
	Hence the output is 1000000000111111122223344444444445555555555666666666

Example Input/Output 2:
	Input:
		19830000189165435362390019123121
	Output:
		10000001111112223333345566889999
'''


a=input().strip()
b=[]
for i in range(10): 
	b.append(0)

for i in a:
	b[int(i)]+=1
c=""

for i in range(1,10): 
	if str(i) in a: 
		c+=str(i)
		b[i]-=1
		break

for i in range(10): 
	while b[i]>0:
		c+= str(i) 
		b[i]-=1

print(c)
