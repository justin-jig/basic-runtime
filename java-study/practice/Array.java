package practice;

import java.util.Scanner;

public class Array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.print("5개의 정수를 입력하세요.");
		Scanner scan = new Scanner(System.in);
		 // 크기가 5인 int 배열
		int [] intArray = new int [5];
		int sum = 0;
		for (int i= 0; i< intArray.length; i++) {
			intArray[i] = scan.nextInt();
			sum += intArray[i];
		}
		scan.close();
		System.out.printf("평균은 %.2f", (double)sum/intArray.length);
		
	}
}
