package studyBasic;


interface MainClass_inter {
    public static final String test = null;
    public static final String test22 = null;
    public static final String test33 = null;
    
	
}

public class MainClass implements MainClass_inter {

	
	static String test = "222";
	static String test22 = "333";
	
	/** instanceof 
	 * 객체가 특정 클래스나 인터페이스의 인스턴스 인지 확인하는 연사자
	 * 
	 * */
	

	public static void main(String[] args) {
		
		System.out.print("안녕하세요");
		System.out.print(test);
		System.out.printf("%d * %d = %d", 10, 2, 10*2).println();
		
		System.out.println(test);
		
		// 형식 지정자
		// %d : 정수, %f : 실수, %s : 문자열, $c : 문자, %b : 블리언
 		
	}
	
	
	

}
