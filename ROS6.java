/* 
@author: Nitya Sunkad

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
*/
import java.util.Scanner;
import java.io.File;

class Main {

  public static int hammingDistance(String s, String t)
  {
    int dist = 0;
    for(int i=0; i<s.length();i++)
    {
      if(!s.substring(i,i+1).equals(t.substring(i,i+1))
        )
      {
        dist++;
      }
    }
    return dist;
  }
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a DNA string (ex: GATTACA) : ");
    String s = sc.next();
    System.out.print("\n"+"Enter another DNA string of equal length to first DNA string (ex: CATTAAA) : ");
    String t = sc.next();
    if(s.length()!=t.length())
    {
      System.out.println("\n"+"Both DNA strings must be the same length. Run and try again.");
    }
    else
      System.out.println("\n"+"The Hamming distance is "+hammingDistance(s,t)+" nucleotides.");

  }

  // Helpful information: Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

}
