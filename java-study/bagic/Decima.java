package studyBasic;

import java.math.BigDecimal;

public class Decima {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		BigDecimal a = new BigDecimal("0.2");
		BigDecimal b = new BigDecimal("0.1");
		
		
		BigDecimal sum1 = a.add(b); // 덧셈
		BigDecimal diff = a.subtract(b); // 밸셈
		BigDecimal muti = a.multiply(b); // 곱셈
		BigDecimal divi = a.divide(b); // 나누셈
		
		
		System.out.println("뺄셈 " + sum1);
		
		
	
	}	

	
	
	
}
