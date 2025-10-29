package arrayStudy;

import java.util.arrayStudys;
import java.util.Scanner;

public class arrayStudyone {
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		/** 방법1. for문을 이용해서 출력 */
		int [] intarrayStudy = {1,2,3,4,5};
		for (int i = 0; i < intarrayStudy.length; i++) {
				
			System.out.println(i);
		}
		
		/** 방법2. tostring을 이용해서 출력 */
		Scanner scan = new Scanner(System.in);
		 // 크기가 5인 int 배열
		int [] intarrayStudy2 = new int [5];
		System.out.println("숫자 5개를 입력하세요");
		for (int i= 0; i< intarrayStudy2.length; i++) {
			intarrayStudy2[i] = scan.nextInt();
		}
		scan.close();
		System.out.println(intarrayStudy2);
		System.out.println(arrayStudys.toString(intarrayStudy2));
	
		/** 방법3. for each문 사용 **/
		for (int arr: intarrayStudy2) {
			System.out.print(arr + " ");
		}
	
	}
}
