'''
In a class, there are N students who are numbered from 1 to N. Each student has taken at least one exam. The program must accept a list of student records as the input. Each record contains two integers representing the student number and the marks scored by the student in an exam. The program accepts one more integer X as the input. The program must print the marks that the Xth student needs to score higher in the class (i.e., the only top scorer).

Boundary Condition(s):
	1 &lt;= N &lt;= 100
	1 &lt;= X &lt;= N
	1 &lt;= Value of each marks &lt;= 100

Input Format:
	The first line contains N and X separated by a space.
	The rest of the lines each contain two integers representing the student number and the marks scored by the student.

Output Format:
	The first line contains an integer representing the marks that the Xth student needs to score higher in the class.

Example Input/Output 1:
	Input:
		3 1
		1 40
		1 60
		2 50
		3 60
		2 40
		3 60
	Output: 
		21
	Explanation: 
		Here X = 1.
		The total marks of the 1st student is 100 (40+60).
		The total marks of the 2nd student is 90 (50+40).
		The total marks of the 3rd student is 120 (60+60).
		Here, the 3rd student scored the highest score in the class.
		The 1st student needs 21 marks to get the highest score in the class. Hence the output is 21

Example Input/Output 2:
	Input:
		5 2
		1 90
		3 50
		2 35
		4 45
		5 40
		3 80
		5 95
		2 67
		5 82
	Output: 
		116
'''

n, x =map(int,input().split())
d = dict()
for i in range(1,n+1):
	d[i]=0
mm = 0

while True:
	try: 
		a, b=map(int, input().split())
		d[a] +=b
		if d[a]>mm:
			mm = d[a]
	except:
		break
c=0

for i in range(1,n+1):
	if d[i]==mm:
		c+=1
if d[x]==mm:
	if c>1:
		print(1)
	else:
		print(0)
else:
	print(mm-d[x]+1)