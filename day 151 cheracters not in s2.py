'''
The program must accept two string values S1 and S2 as the input. The program must print the number of characters in the string S1 that are not present in the string S2 as the output.

Boundary Condition(s):
	1 <= Length of S1, S2 <= 100

Input Format:
	The first line contains S1.The second line contains S2.

Output Format:
	The first line contains the number of characters in the string S1 that are not present in the string S2.

Example Input/Output 1:1
	Output: 
		4
	Explanation:
		The four characters in the string skillrack that are not present in thestring rockstar are i, I, I and k.

Example Input/Output 2:
	Input:
		SolarSystem
		satellite
	Output: 
		6
	Explanation:
		The six characters in the string SolarSystem that are not present in the string satellite are S, o, r, S, y and m.
'''
a=input().strip()
b=input().strip()
c=set(a)
s=0
for i in c:
	if a.count(i)>b.count(i):
		s+=a.count(i)-b.count(i)
print(s)