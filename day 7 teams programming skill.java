/*
There are N students in a class (where N is always even). Each student has programming skill which is represented by an integer. The class tutor wants to form N/2 teams based on the following conditions.

-Each team should consist of exactly two students. -Each student should belong to exactly one team.
-Two students can form a team only if their programming skills are equal. Students can solve problems to increase their programming skill. If a student solves K problems then his/her programming skill is increased by K. The class tutor wants to know the minimum total number of problems T required by the students to form exactly N/2 teams.
The program must accept N integers representing the programming skill of N students as the input. The program must print the value of T as the output.

Boundary Condition(s):
	2 <= N <= 10^4
	1 <= Each integer value <= 1000

Input Format:
	The first line contains N. The second line contains N integers separated by a space.

Output Format: 
	The first line contains T,

Example Input/Output 1:

	Input
		6
		5 10 23 14 5
	
	Output	
		5
	
	Explanation:
		The three possible teams are (5, 5), (10, 14) and (2, 3). In the first team, their programming skills are equal (5, 5). In the second team, their programming skills are not equal (10, 14). To make them equal, one of the students need to solve 4 problems. In the third team, their programming skills are not equal (2, 3). To make them equal,one of the students need to solve 1 problem.
So totally 5 problems are required to form three teams.

Example Input/Output 2:
	Input
		2
		40 100
	Output
		60
*/



import java.util.*; 
public class Hello 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(); sc.nextLine();
		int arr[] = new int[a], sum = 0; 
		for(int i=0;i<a; arr[i++]=sc.nextInt()); 
			Arrays.sort(arr);
		for(int i=0;i<a; i+=2) 
		{ 
			sum += arr[i+1]-arr[i];
		}
		System.out.println(sum);
	}
}
