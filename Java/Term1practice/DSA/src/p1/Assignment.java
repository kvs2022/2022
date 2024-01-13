package p1;
import java.util.*;
public class Assignment {
			public static void main(String[] args) 
			{
			Stack st=new Stack();
			
			Scanner sc=new Scanner(System.in);
			
		
			
			int item;
			//size of the stack
		int max;
		System.out.println("Enter the size of the stack=");
		max=sc.nextInt();
		//current size of the stack
		System.out.println("Enter the current number of elements in the stack=");
		int n=sc.nextInt();
		
		for (int i=0;i<n;i++) {
			int m;
			System.out.println("Enter " + (i+1) +"th element in the stack=");
			m=sc.nextInt();
			st.push(m);

		}
		
		System.out.println("Stack="+st);
		
		if (n==max) {
			System.out.println("Stack overflow");
			System.exit(n);
		}
		
		
		else 
			n+=1;
		System.out.println("Enter the element to be pushed=");
			item=sc.nextInt();
			st.push(item);
			System.out.println("Stack after insertion ="+st);
			
		}
		
	  
	}
}
