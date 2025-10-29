package practice;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ClassRectangleContainer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		ArrayList<ClassRectangle> list = new ArrayList<>();
		Scanner scan = new Scanner(System.in);
		
		try {
		
			while(true) {
			
				System.out.println("width값 , height값은??");
				double width = scan.nextDouble();
				double height = scan.nextDouble();
				
				if (width == 0 && height == 0) break;
				
				ClassRectangle rectangle  = new ClassRectangle(width);
				rectangle.setHeight(height);
				list.add(rectangle);
				
			}
			
			
		} catch ( InputMismatchException e) {
			
			System.out.println("문자열은 안됩니다.");
		}
		
		for ( ClassRectangle rect: list) {
			
			System.out.printf("width ? :: %.0f", rect.getWidth()).println();
			System.out.printf("height ? :: %.0f", rect.getHeight()).println();
			System.out.printf("넓이는 ? :: %.0f", rect.rectangleSize()).println();
			
			System.out.println("--------------------------------------------------------------");
		}
			
		System.out.printf("Rectangle 인스턴스의 개수는 :: %d",ClassRectangle.count).println();;
	
	
	}

}
