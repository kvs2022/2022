package pkg1;
import java.util.*;

public class AgeException{
	String breed = "Doggssss";
	static String n1;
	static String n2;
	static String n3;
	static String n4;
	static String n5;
	
	public static void main(String[] args) {
		AgeException d=new AgeException();
		Scanner sc=new Scanner(System.in);
		System.out.println("Name of 1st dog");
		n1=sc.next();
		System.out.println("Name of 2nd dog");
		n2=sc.next();
		System.out.println("Name of 3rd dog");
		n3=sc.next();
		System.out.println("Name of 4th dog");
		n4=sc.next();
		System.out.println("Name of 5th dog");
		n5=sc.next();
		System.out.println("Name of the breed "+d.breed);
		
		

	}

}
