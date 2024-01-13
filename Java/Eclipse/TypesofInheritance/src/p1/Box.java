package p1;

public abstract class Box {
	float side;
	abstract float findArea();
	//abstarct as we don't want to implement this
}
class SquareBox extends Box
{
	public SquareBox() {
		super.side=5.5f;
	}
	float findArea() {
		return side*side;		
	}
}

class Rectangle
{
	public static void main(String ar[]) {
		System.out.println("People are mean they are shittty");
	}
}