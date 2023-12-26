'''
The program must accept all the possible pairs of positive integers except one pair, where the sum of two integers in each pair is equal to N as the input. The program must print the missing pair of integers which gives the sum N as the output. Note: The integers in each pair are always sorted in ascending order.

Boundary Condition(s): 
	1 <= Each integer value <= 1000

Input Format:
	The first line contains a list of pairs separated by a space, where each pair contains two integers separated by a comma and enclosed within parentheses.

Output Format:
	The first line contains two integers separated by comma and enclosed within parentheses.

Exampla Input/Output 1:
	Input
		(1,4)
	Output
		(2,3)
	Explanation:
		The two possible pairs that give the sum 5 are (1,4) and (2,3). 
		Here, the missing pair is (2,3). 
		So (2,3) is printed as the output.

Example Input/Output 2:
	Input
		(10,10) (4,16) (1,19) (2,18) (7,13) (6,14) (9,11) (3,17) (5,15)
	Output 
		(8,12)

Example Input/Output 3:
	Input: 
		(3,3) (2,4)
	Output 
		(1,5)


'''

l=list(map(str, input().split()))
z=[]
x=[]
for i in range(len(1)):
	q,w=1[i].split(",")
	q=int(q[1:])
	w=int(w[:-1])
	z.append(q)
	x.append(w)
	if i==0:
		m=int(z[0])+int(x[0])
e=max(z)
r=max(x)
t=max(e,r)

for i in range(1,t):
	if i not in z:
		print("("+str(i)+", "+str(m-1)+")")
		exit()