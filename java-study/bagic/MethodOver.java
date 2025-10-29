package studyBasic;

public class MethodOver {

	
	/**
	 * 메소드 오버로드
	 * 정수 두개를 더하는 메소드
	 */
	
	//정수 더하는 메소드
	public int add (int a, int b) {
		return a + b;
	}

	public int add (int a, int b , int c) {
		
		return a + b + c;
	}
	
	
	//실수 더하는 메소드
	public double add (double a, double b) {
		return a + b;
		
	}
	public double add (double a, double b, double c) {
		return a + b + c;
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		MethodOver calc = new MethodOver();
	
		System.out.println(calc.add(5, 4));
		System.out.println(calc.add(5, 4, 7));
		System.out.println(calc.add(5.1, 4.1));
		System.out.println(calc.add(5.1, 4.1, 6.4));
	
	}

}
