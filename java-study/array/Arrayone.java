package array;

import java.util.Arrays;
import java.util.Scanner;

public class Arrayone {
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		/** 방법1. for문을 이용해서 출력 */
		int [] intArray = {1,2,3,4,5};
		for (int i = 0; i < intArray.length; i++) {
				
			System.out.println(i);
		}
		
		/** 방법2. tostring을 이용해서 출력 */
		Scanner scan = new Scanner(System.in);
		 // 크기가 5인 int 배열
		int [] intArray2 = new int [5];
		System.out.println("숫자 5개를 입력하세요");
		for (int i= 0; i< intArray2.length; i++) {
			intArray2[i] = scan.nextInt();
		}
		scan.close();
		System.out.println(intArray2);
		System.out.println(Arrays.toString(intArray2));
	
		/** 방법3. for each문 사용 **/
		for (int arr: intArray2) {
			System.out.print(arr + " ");
		}
	
	}
}
