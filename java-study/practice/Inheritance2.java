package practice;

import java.util.StringTokenizer;

class Vehicles {
	
	boolean license = false;
	String color = "";
	
	public Vehicles (boolean license, String color) {
		
		this.license = license;
		this.color = color;
		
	}
	
	public String getInfo() {
		return ",license :: " + license + ",color ::  " + color;
	}
	
}

class Car extends Vehicles {
	
	String kind = "";
	
	public Car (String kind, boolean license, String color ) {
		super(license, color);
		this.kind = kind;
		
	}	
	
	public String getInfo() {
		return "kind :: " + kind + super.getInfo();
	}
	
}

public class Inheritance2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		 
		Car car = new Car("자동차", true, "파랑색");
		
		StringTokenizer token = new StringTokenizer(car.getInfo(), ",");
		
		System.out.println(token.nextToken());
		System.out.println(token.nextToken());
		System.out.println(token.nextToken());
	}

}
