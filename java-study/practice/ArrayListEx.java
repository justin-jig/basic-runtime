package practice;

import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ArrayList <String> list = new ArrayList<>();
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
