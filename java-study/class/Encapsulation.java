package studyClass;


/** Encapsulation : 은닉화 */


public class Encapsulation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		EnCar bmw = new EnCar(10);
		EnCar kia = new EnCar(20);
		
	
		/** 잘못된 접근 방식 */
		bmw.speed = 120;
		kia.speed = 100;
		bmw.start();
		kia.start();
		
		/** 유효성 검사 예외 처리, 클래스 보호 */
		bmw.setSpeed(-120);
		kia.setSpeed(-120);
		
		/** getter setter */
		bmw.setSpeed(120);
		System.out.println("bmw getter ::" + bmw.getSpeed());

		kia.setSpeed(200);
		System.out.println("kia getter ::" + kia.getSpeed());
		
		
		/** 증감 */
		bmw.increaseSpeed(100);
		System.out.println("bmw 증감 ::" + bmw.getSpeed());

		kia.increaseSpeed(80);
		System.out.println("kia 증감 ::" + kia.getSpeed());
		
		/** 감소 */
		bmw.decreaseSpeed(40);
		System.out.println("bmw 감소 :: " + bmw.getSpeed());

		kia.decreaseSpeed(60);
		System.out.println("kia 감소 :: " + kia.getSpeed());
		
		
		
	}

}


