/*
The program must accept an integer matrix of size NxN as the input. The program must print all the diagonal elements of the matrix in circularly clockwise direction as the output

Boundary Condition(s): 
	2 <= N <= 100
Input Format:
	The first line contains N.
	The next N lines contain N integers each separated by a space.

Output Format:
	The first line contains all the diagonal elements of the matrix separated by a space.

Example Input/Output 1:
	Input
		4
		1 2 3 4 
		5 6 7 8
		9 10 11 12 
		13 14 15 16
	Output
		1 4 16 13 6 7 11 10
	Explanation
		In the 4x4 matrix, all the diagonal elements are highlighted below
		1 2 3 4
		5 6 7 8
		9 10 11 12
		13 14 15 16
		So the diagonal elements are printed in the circularly clockwise direction.
Hence the output is 1 4 16 13 6 7 11 10

Example Input/Output 1:
	Input
		3
		10 20 30
		40 50 60
		70 80 90
	Output:
		10 30 90 70 50
*/
import java.util.*; 
public class Hello 
{
	public static void check(int arr[][], int t, int n) 
	{ 
		System.out.print(arr[t][t]+" ");
		System.out.print(arr[t][n-t-1]+" "); 
		System.out.print(arr[n-t-1][n-t-1]+" ");
		System.out.print(arr[n-t-1][t]+" ");
	}
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in); 
		int a = sc.nextInt(); 
		int arr[][] = new int[a][a]; 
		for(int i=0;i<a;i++) 
		{ 
			for (int j=0;j<a;arr[i][j++]=sc.nextInt());
		} 
		for (int i=0;i<a/2;i++) 
			check(arr,i,a); 
		if(a%2==1) 
			System.out.print(arr[a/2][a/2]);
	}
}