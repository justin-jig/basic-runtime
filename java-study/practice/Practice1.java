package practice;

import java.util.Scanner;

public class Practice1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scanner = new Scanner(System.in);
		
		try {
			
			System.out.print("이름을 입력하세요");
			String name = scanner.next();
			System.out.print("나이을 입력하세요");
			int age = scanner.nextInt();
			
			System.out.printf("안녕하세요! %s님 (%d)세", name, age);
			
		} catch(Exception e) {
			
			System.out.print("제대로 입력하세요");
		}
		
		scanner.close();
	}

}
