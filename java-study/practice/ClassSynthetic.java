package practice;

abstract class Vehicle {
	
	private String name ;
	private int maxSpeed ;
	abstract void move();
	abstract void speed();
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public int getMaxSpeed() {
		return maxSpeed;
	}


	public void setMaxSpeed(int maxSpeed) {
		this.maxSpeed = maxSpeed;
	}

}


interface Flayable {
	void fly();
}

class Car1 extends Vehicle {

	public Car1 (String name, int maxSpeed) {

		super.setName(name);
		super.setMaxSpeed(maxSpeed);
	}
	@Override
	void move() {
		// TODO Auto-generated method stub
		System.out.println("도로를 따라 이동 중");
	}
	@Override
	void speed () {
		
		System.out.printf( "%s 속도는 : %d",super.getName(), super.getMaxSpeed() ).println();
	}
	
}

class Airplane extends Vehicle implements Flayable {

	public Airplane (int maxSpeed) {

		super.setName("Boeing");
		super.setMaxSpeed(maxSpeed);

	}
	@Override
	public void fly() {
		// TODO Auto-generated method stub
		System.out.println("고도 10,000피트에서 비행 중");
	}

	@Override
	void move() {
		// TODO Auto-generated method stub
		System.out.println("하늘을 날아가는 중");
	}
	@Override
	void speed () {
		
		System.out.printf( "%s 속도는 : %d",super.getName(), super.getMaxSpeed() ).println();
	}

}




public class ClassSynthetic {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Vehicle [] arr = {new Car1("bmw", 100), new Airplane(1000)};

		for (Vehicle ins : arr) {
			
			ins.speed();
			ins.move();
			
			/** instanceof: 객체가 트정 클래스나 인터페이스의 인스턴스인지 확인하는 연산자 */
			if  ( ins instanceof Flayable) {
				((Flayable) ins).fly();
				
			}
		}

	}

}
