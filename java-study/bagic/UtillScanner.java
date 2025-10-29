package studyBasic;

import java.util.Scanner;

public class UtillScanner {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		/**
		 * Scanner 
			• next() : 공백 이전까지의 문자열을 읽음.
			• nextLine() : 엔터(\n) 이전까지의 문자열을 읽음.
		*/
		
		System.out.println("이름, 나이, 키, 결혼 여부를 빈칸으로 분리하여 입력하세요.");
		Scanner scanner = new Scanner(System.in);
		
		try {
			
			String name = scanner.next(); // 공백 이전까지의 문자열 읽기
			int age = scanner.nextInt(); // 정수 읽기
			double height = scanner.nextDouble(); // 실수 읽기
			boolean single = scanner.nextBoolean(); // 블리언 읽기
			System.out.printf("이름은 %s 나이는 %d 키는 %.1f, 결혼은 %b", name,age, height, single);
			
		} catch(Exception  e) {
			
			System.out.print("제대로 입력해주세요");
		}
		
		scanner.close();
		
	}

}
