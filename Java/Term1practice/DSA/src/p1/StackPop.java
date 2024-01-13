package p1;
import java.util.*;
public class StackPop {
		public static void main(String[] args) {
			
			Stack<Integer> s1=new Stack<Integer>();
			s1.push(11);
			s1.push(10);
			s1.push(1);
			s1.push(5);
			
			System.out.println("The initial stack is: "+s1);
			//popping elements from top of the stack
			System.out.println("The element that is popped: "+s1.pop());
			System.out.println("The element that is popped: "+s1.pop());
			System.out.println("The final stack is: "+s1);

		}

	}

