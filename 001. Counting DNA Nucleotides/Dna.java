/* 
@author: Nitya Sunkad, 2020

PROBLEM 1: Counting DNA Nucleotides

*** Given: A DNA string s of length at most 1000 nt (nucleotides, 'A', 'C', 'G', 'T')

*** Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
*/

import java.util.Scanner;

class Main {
  
private static String numberOfNucleotides(String str)
{
int a=0; 
int t=0;
int c=0;
int g=0;
for(int i=0; i<str.length();i++)
{
  String x=str.substring(i,i+1);
  if(x.equals("A"))
    a=a+1;
  if(x.equals("T"))
    t=t+1;
  if(x.equals("C"))
    c=c+1;
  if(x.equals("G"))
    g=g+1;
	
}
  String s=(a+" "+c+" "+g+" "+t); //number of A's, number of C's, number of G's, and number of T's in the input strand of DNA
  return s;
}

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a DNA string (ex: GATTACA): ");
    String s = sc.next();
    System.out.print("The number of A's, C's, G's, and T's, respectively, in the input DNA string are "+ "\n"+numberOfNucleotides(s));
    
   
  }
}
