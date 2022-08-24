/* 
@author: Nitya Sunkad

PROBLEM 2: Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

*** Given: A DNA string t having length at most 1000 nt.

*** Return: The transcribed RNA string of t.
*/

import java.util.Scanner;

class Main {
  private static String thymineToUracil(String cStr)
  {
    String tStr="";
    {
    	for(int i=0; i<cStr.length();i++)
    	{
        if(cStr.substring(i,i+1).equals("T"))
          tStr=tStr+"U";
        else
          tStr=(tStr+cStr.substring(i,i+1));
      } 			
    }
    return tStr; //transcribed RNA string (when DNA is converted to RNA, all the T's (thymine) are converted to U's (uracil).

  }
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a DNA string (ex: GATTACA): ");
    String s = sc.next();
    System.out.println("The RNA translation of the input DNA string is: "+thymineToUracil(s));
  }
}
