package studyBasic;

import java.util.Scanner;

public class Condition {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		try {
			System.out.print("수를 입려하세요 : ");
			
			// if else
			int num = scan.nextInt();		
			if ( num % 3 == 0 ) {
				System.out.println("3의 배수입니다.");

			} else {
				System.out.println("3의 배수가 아닙니다.");
			}
			
			// switch 문
			switch (num % 3) {
				case 0:
					System.out.println("3의 배수입니다.");
				break;
				
				default : System.out.println("3의 배수가 아닙니다.");
			}
			
			
		} catch ( Exception e) {
			System.out.print(e);
	
		}
		scan.close();
		
		/**
		 * 문자열 비교
		 * 자바에서 문자열은 String 자료형(래퍼런스자료형)이므로, 변수로 접근할 수 있는 값은 문자열이 저장된
		 * 메모리 주소값입니다. 따라서 == 연산자로는 비교가 불가능.
		 * 변수.equals("문자열") 형태로 비교해야함.
		 */
		
		
		Scanner scan2 = new Scanner(System.in);
		try {
			System.out.print("이름을 입려하세요 : ");
			
			// if else
			String name = scan2.nextLine();		
			if ( name.equals("") ) {
				System.out.println("코딩온님 환영합니다.");

			} else {
				System.out.printf("%s님 환영합니다.", name);
			}
			
			
			
		} catch ( Exception e ) {
			
			System.out.print(e);
	
		}
		scan2.close();

	}

}
