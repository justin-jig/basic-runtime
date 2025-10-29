package studyClass;


interface Move {
	void moveForward();
	void moveBackword();
}

interface Power {
	void powerOn();
	void powerOff();
}

// 인터페이스는 인터페이스를 상속 받을 수 있음.
// 다중 상속이 가능
interface Car extends Move, Power { // 다중 상속
	void changeGear(int gear);
	
}

class SUV implements Car {

	@Override
	public void moveForward() {
		// TODO Auto-generated method stub
		System.out.println("전친");
	}

	@Override
	public void moveBackword() {
		// TODO Auto-generated method stub
		System.out.println("후진");
	}

	@Override
	public void powerOn() {
		// TODO Auto-generated method stub
		System.out.println("시동 ON");
	}

	@Override
	public void powerOff() {
		// TODO Auto-generated method stub
		System.out.println("시동 OFF");
	}

	@Override
	public void changeGear(int gear) {
		// TODO Auto-generated method stub
		System.out.println("기어 변경 ::" + gear);
	}
	
}

public class JavaInterface2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		SUV suv = new SUV();
		
		suv.powerOn();
		suv.moveForward();
		suv.changeGear(1);
		suv.moveBackword();		
		suv.powerOff();


	}

}
