package studyClass;



// static 없는 경우
class WitoutStatic {
	
	private int registered = 0;
	private String name;
	
	public WitoutStatic(String name) {
		this.name = name;
		registered ++;
	}

	public int getRegistered() {
		return registered;
	}
	
	

}

//static 변수가 있는 경우
class WidthStatic {
	private static int registered = 0;
	private String name;
	
	public WidthStatic(String name) {
		this.name = name;
		registered ++;
	}

	public int getRegistered() {
		return registered;
	}

}

// static 메소드

class MathUtil {
	
	static double PI = 3.14;
	
	// 메소드
	public static double cricle (double redius) {
		
		return PI * redius * redius;
	}
	
	
}


public class CompareStatic {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/** static이 없는 경우 */
		WitoutStatic a = new WitoutStatic("홍길동");
		WitoutStatic b = new WitoutStatic("이몽룡");
		
		System.out.println("WitoutStatic");
		System.out.println("홍길동 :: " + a.getRegistered());
		System.out.println("이몽룡 :: " + b.getRegistered());
		
		
		/** static이 있는 경우 */
		WidthStatic c = new WidthStatic("성춘향");
		WidthStatic d = new WidthStatic("임꺽정");
		WidthStatic e = new WidthStatic("임꺽정");
		System.out.println("WidthStatic");
		System.out.println("성춘향 :: " + c.getRegistered());
		System.out.println("임꺽정 :: " + d.getRegistered());
		System.out.println("임꺽정 :: " + e.getRegistered());
		
	
		System.out.printf("원의 넓이 :: %.1f" , MathUtil.cricle((double) 3.5)).println();
	}

}
