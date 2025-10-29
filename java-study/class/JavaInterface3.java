package studyClass;


interface Constants {
	
	/** final 키워드
	 * 
	 * 클래스에서 사용 : 상속될 수 없다. final class MyClass {}
	 * 매소드에서 사용 : 오버라이드 될 수 없다.
	 * 변수에서 시용 : 값 변경 불가능, 상수가 됨.
	 * 배개 변수에서 사용 : 매개변수 값 변경 불가능. void function(fina int x ) {}
 	 */
	public final int MAX_VALUE = 100;
	
	// public final이 생략되었음.
	double PI = 3.14;
	
}

class ConstantsEx implements Constants {
	void display () {
		System.out.println("MAX_VALUE"+ MAX_VALUE);
		System.out.println("PI" + PI);
		
	}
	
}


public class JavaInterface3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ConstantsEx ex = new ConstantsEx();
		ex.display();
		
	}

}
