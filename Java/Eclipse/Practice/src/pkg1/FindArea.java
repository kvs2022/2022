package pkg1;

public class FindArea extends Rectangular{

	@Override
	float FindArea() {
		float Area=width*length*no_of_rooms;
		return Area ;
	}
	public static void main(String[] args) {
		Rectangular r1=new FindArea();
		r1.length=7;
		r1.width=8;
		r1.no_of_rooms=2;
		System.out.println("Area= "+r1.FindArea());
	}
}