
package pkg1;
public class Employee
{
	private String id;
	private Employee(String id)
	{
		this.id="563458";
		id=id+"DEF";
		System.out.println(id);
		System.out.println(this.id);
	}
	
	public static void main(String[] args) {
		new Employee("123"); 
	}
}

