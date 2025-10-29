package practice;

import java.math.BigDecimal;
import java.util.Scanner;

public class Condition {

	public void Practice1 () {
	 
		Scanner scan = new Scanner(System.in);
		System.out.print("나이를 입력하세요 : ");
		
		try {
			
			int age = scan.nextInt();
			// 1~ 7 까지가 유아
			// 8~ 13 까지가 초등학생
			// 14 ~ 16 까지가 중학생
			// 17 ~ 19 까지가 고등학생
			// 20 부터 성인
			
			if (age <= 0) {
				System.out.print("1세 이상 입력해주세요");
			} else if (age < 8) {
				System.out.print("유아");
				
			} else if (age < 14) {
				System.out.print("초등학생");
				
			} else if (age < 18) {
				System.out.print("중학생");
				
			} else if (age < 20) {
				
				System.out.print("고등학생");
			} else {
				System.out.print("성인");
			}
			
		} catch(Exception e) {
			
			System.out.print("정수형으로 입력해주세요.");
		}
		
		scan.close();
	}	
	
	public void Practice2 () {
		
		Scanner scan2 = new Scanner(System.in);
		System.out.print("이름을 입력하세요 : ");
		
		try {
			
			String name = scan2.nextLine();

			if (name.equals("홍길동")) {
				System.out.print("남자");
			} else if (name.equals("성춘향")) {
				System.out.print("여자");
				
			} else {
				System.out.print("모르겠어요");
			}
			
		} catch(Exception e) {
			
			System.out.print("정수형으로 입력해주세요.");
		}
		
		scan2.close();
		
	}
	
	
	public void Practice3 () {
		
		Scanner scan2 = new Scanner(System.in);
		System.out.print("숫자를 2개 입력하세요");
		
		try {
			
			int nu1 = scan2.nextInt();
			int nu2 = scan2.nextInt();
			
			System.out.printf("덧셈 결과 %d", nu1 + nu2).println();
			System.out.printf("뺄셈 결과 %d", nu1 - nu2).println();
			System.out.printf("곱하기 결과 %d", nu1 * nu2).println();
			System.out.printf("나눗셈 결과 %d", nu1 / nu2).println();

			
		} catch(Exception e) {
			
			System.out.print("정수형으로 입력해주세요.");
		}
		
		scan2.close();
		
	}
	
	
	public static double circleCalc (double a) {
		
		double pi = Math.PI;
		return  pi * (a * a) ;
	}
	public static int rectangleCalc (int a, int b) {
		
		
		return a * b;
	
	}
	
	public static double triangleCalc (int a, int b) {
		
		
		return (a * b) / 2;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Condition practice = new Condition();
		
		

//		double redius = 5;
//		double re = practice.circleCalc(redius);
//		double re2 = practice.rectangleCalc(4,7);
//		double re3 = practice.triangleCalc(6,3);
//		System.out.printf("원의 반지름 5의 넓의는 %.5f", re).println();
//		System.out.printf("직사각형 가로 5 세로 7인 넓이는 %.1f", re2).println();
//		System.out.printf("삼각형 밑변 6의 높이 3의 넓이는 %.1f", re3).println();
		
		
		
		
	}

}

