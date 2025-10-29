package studyClass;



interface Controller {
	void powerOn();
	void powerOff();
	default void display() {
	
		System.out.println("디스플레이가 켜졌습니다.");
		
	}
	
}

class TV implements Controller {
	
	@Override
	public void powerOn() {
		System.out.println("TV power ON");
	};
	
	@Override
	public void powerOff() {
		
		System.out.println("TV power OFF");
	};
	
}

class Computer implements Controller {

	@Override
	public void powerOn() {

		System.out.println("Computer power ON");
	}

	@Override
	public void powerOff() {
		
		System.out.println("Computer power OFF");
	}
	
	
}


public class JavaInterface1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		TV tv= new TV();
		tv.powerOn();
		tv.display();
		tv.powerOff();
	
	}
	
}
