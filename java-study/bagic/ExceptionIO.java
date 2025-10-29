package studyBasic;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionIO {

	public  void exception1 () {
		
		/** 0으로 나눈 경우 **/
		int num1 = 4;
		int num2 = 0;
		
		try {
		
			System.out.println(num1 + "/" + "=" + (num1/num2));
			
		} catch ( ArithmeticException e ) {
			
			System.out.println("0으로 나누어 예외가 발생하였습니다.");
		}
		
	}
	
	public void exception2 () {
		
		/** 인덱스 범위를 벗어났을 때 **/
		int[] intArray = {1,2,3,4};
		
		try {
			for(int i = 0; i < 5; i++ ) {
				System.out.println(intArray[i]);
			}
			
		} catch ( ArrayIndexOutOfBoundsException e ) {
			System.out.println("인덱스 범위가 벗어났습니다.");
		}
		
	}
	
	public  void exception3 () {
		
		/** 입력 오류 **/
		Scanner scan = new Scanner(System.in);
		System.out.println("정수를 입력하세요.");
		
		try {
			
			int num = scan.nextInt();
	
		} catch ( InputMismatchException e ) {
			System.out.println("정수 입력 오류");

		}
		
		scan.close();
		
	}

	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ExceptionIO output = new ExceptionIO();
			
		output.exception1();
		output.exception2();
		output.exception3();
		
		/** 숫자 오류  NumberFormatException **/
		/** 파일 존재 하지 않을 때 오류 (컴파일러에 의해 체크됨)  FileNotFindException **/
		/** 객체 참조가 null 인 상태에서 객체 매서드나 속성에 접근할때 NullPointerExeption **/
	
	}

}
