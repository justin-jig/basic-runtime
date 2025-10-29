package practice;

import java.util.arrayStudyList;
import java.util.Scanner;

public class arrayStudyListEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		arrayStudyList <String> list = new arrayStudyList<>();
		Scanner scan = new Scanner(System.in);
		
		while (true) {
			
			System.out.println("문자를 입력해주세요. : ");
			String insert = scan.nextLine();
			if (insert.equals("exit"))  break; 
			list.add(insert);
			
		}	
		scan.close();
		//		for ( String a: list) {
		//			System.out.println(a);	
		//		}
		System.out.println(list);
	}
}
