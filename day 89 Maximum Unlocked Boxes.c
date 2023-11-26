/*
Mr. ABC has M boxes and N keys. Each box contains a certain number of gold coins and each key has a number written on it. The number of gold coins in each box and the number written on each key are passed as input to the program. He wants to open as many boxes as possible based on the following conditions.
-If the number of gold coins in a box is even, the key with the odd number is the correct key to open the box.
-If the number of gold coins in a box is odd, the key with the even number is the correct key to open the box.
-A key cannot be used to open more than one box
The program must print the maximum number of boxes he can open based on the given conditions.

Boundary Conditions(s):
	1 <= M N <= 1000
	1 <= Number of gold coins in each box <= 10^8
	1 <= Number written on each key <= 10^8

Input Format:
	The first line contains M and N separated by a space.
	The second line contains M integers separated by a space.
	The third line contains N integers separated by a space.

Output Format:
	The first line contains an integer representing the maximum number of boxes he can open.

Example Input/Output 1:
	Input
		4 3
		8 2 1 7
		2 9 5
	Output
		3
	Explanation:
		The first box contains 8 gold coins. The possible keys to open the box are 9 and 5. Here, we can use the key 9.
		The second box contains 2 gold coins. The only possible key to open the box is 5 (as we used the key 9 to open the first box).
		The third box contains 1 gold coin. The only possible key to open the box is 2.
		The fourth box contains 7 gold coins. There are no keys to open this box. So the maximum number of boxes he can open is 3.
Hence the output is 3

Example Input/Output 2:
	Input
		3 4
		10 8 1
		20 30 40 50
	Output
		1
*/

m,n=map(int,input().split()) 
l=list(map(int, input().split())) 
d=list(map(int, input().split()))
s=0
for i in range(len(1)): 
	for j in range(len(d)): 
		if l[i]%2==0 and len(d)>0: 
			if d[j]%2!=0: 
				s=s+1 
				d.remove(d[j])
				break
		else:
			if len(d)>0 and d[j]%2==0: 
				s=s+1 
				d.remove(d[j]) 
				break
print(s)