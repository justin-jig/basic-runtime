package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class InputBuffer {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//StringBuilder st = new StringBuilder();
		
		System.out.println("가로 세로 크기를 입력하세요.");
		
		try {
			
			// string 쪼개기
			StringTokenizer token1 = new StringTokenizer(br.readLine(), " " , false);
		
			System.out.print(token1.countTokens());
			for (int i=0; i<token1.countTokens(); i++ ) {
				System.out.print(token1.countTokens());
				System.out.println("token" + token1.nextToken());
			}
			
			StringTokenizer token = new StringTokenizer(br.readLine());
			double wd = Double.parseDouble(token.nextToken());
			double he = Double.parseDouble(token.nextToken());
			// int wd = Integer.parseInt(token.nextToken());
			// int he = Integer.parseInt(token.nextToken());
			
			System.out.print(wd);
			System.out.print(he);
			 
			
		} catch(NoSuchElementException e) {
				
			System.out.println(e);
			
		} catch (NumberFormatException e) {
			
			System.out.println(e);
		}
		
	}

}
