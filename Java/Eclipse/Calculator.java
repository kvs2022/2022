package compiletimepoly;

public class Calculator {

	private int n1,n2,total;
	
	//Method Overloading
	void add()
	{
		total=n1+n2;
		System.out.println(total);
	}
	
	int add(int n1,int n2) {
		total=n1+n2;
		return total;
		
	}
	
	float add(float n1,float n2)
	{
		total=(int) (n1+n2);
		return total;
	}
}
