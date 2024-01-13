package lab1;
public abstract class Rectangular {
			
			float width;
		    float length;
		    float no_of_rooms;
		    abstract float findArea();
		    public class Room extends Rectangular {
		    	
		    	public Room(float width, float length, float no_of_rooms){
		    		   this.length=length;
		    		   this.no_of_rooms=no_of_rooms;
		    		}
		    		float findArea(){
		    		 float Area = width*length*no_of_rooms;
		    		 return Area;
}
}
     public class FindArea extends Rectangular {
	@Override
	float findArea() {
		float Area=length*width*no_of_rooms;
		return Area;
	}
	public static void main(String[] args) {
		Rectangular r1=new FindArea();
		r1.length=25;
		r1.width=20;
		r1.no_of_rooms=10;
		System.out.println("Area= "+r1.findArea());
		
	}  
}
}

