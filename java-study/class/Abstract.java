package studyClass;

/** 추상 */

// 추상 클래스
abstract class Animals {
	private int age;
	// 추상 메서드
	abstract public void sound ();
	
	// 일반 메서드
	public void sleep() {
		System.out.println("동물이 잠을 잔다");
	}
}

// 추상클래스 Animal을 상속받는 ChicKEN 클래스
class Chicken extends Animals {
	
	@Override
	public void sound () {
		
		System.out.println("꼬꼬댁");
		
	}
}


public class Abstract {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 추상클래스는 인스턴스화 할 수 없음
		// Animals animals = new Animals();	
		
		Chicken chicken = new Chicken();
		chicken.sound();
		chicken.sleep();
		
		
	}

}
