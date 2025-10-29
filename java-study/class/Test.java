package studyClass;

public class Test {
	
	public long test () {
		
		long t = 1;
		
		return t;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 추상클래스는 인스턴스화 할 수 없음
		// Animals animals = new Animals();	
		
		
		String test = "https://kdt9-justin.s3.ap-northeast-2.amazonaws.com/profileImage/e9d859b3-8321-4e5a-ab56-360700308b67_image.png";
		
		
		String [] t = test.split("amazonaws.com");
		
		for (int i =0 ; i < t.length; i++) {
			
			System.out.println(t[i]);
		}
 		
		Test test1 = new Test();
		System.out.println(test1.test());

		System.out.println(t[1].substring(1));
		
		
	}

}
