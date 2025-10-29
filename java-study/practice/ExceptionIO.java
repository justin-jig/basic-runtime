package practice;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;


public class ExceptionIO {
	
	
	public void exception1 () {
		int [] intArray = {1,2,3,4};

		try {
			
			for (int i = 0; i < 5; i++) {
				System.out.println(intArray[i]);
			}
			
		} catch (ArrayIndexOutOfBoundsException e ){
			System.out.println("인덱스 범위를 벗어났습니다.");
		}
	}
	
	
	public void exceoption2 () {
		
		Scanner scan = new Scanner(System.in);	
		
		try {
			
			System.out.println("배열의 크기를 입력해주세요.");
			int size = scan.nextInt();
			int[] list = new int[size];
			int i = 0;
			int sum = 0;
			while ( i < size) {
				
				System.out.printf("배열의 %d번째 value입력해주세요.", i + 1).println();
				
				int result = scan.nextInt();
				list[i] = result; 
				sum += result;
				i++;
			}
			System.out.printf("입력값 :: %s", Arrays.toString(list)).println();
			System.out.printf("평균은 ? :: %.2f", (double)sum/list.length);		
		
		} catch ( InputMismatchException e) {
			
			System.out.println("정수만 가능합니다.");
		}
		
	}
	
	public static void main(String[] args) {
		
		ExceptionIO ouput = new ExceptionIO();
		
		ouput.exceoption2();
		
	}
}
