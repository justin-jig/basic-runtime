package studyClass;

import java.util.ArrayList;

public class WrapperClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		/**
		 * Wrapper 클래스
		 * 8가지 기본 데이터 타입(primitive data type)을 객체로 표현하기 위한 클래스
		 * Byte, Shot, Float, Double, Integer, Character, Long, Boolean
		 * Null 값 허용 기본 테이터 타입은 x
		 */
		
		/**
		 * auto-boxing : 기본 데이터 타입을 Wrapper 클래스 객체로 자동 변환
		 * auto-unboxing : Wrapper 클래스 객체를 기본 데이터 타입으로 자동 변환
		 */
		
		ArrayList <Integer> numbers = new ArrayList<>();
		numbers.add(1); // 오토 박싱으로 int가 integer로 변환되어 저장됨
		numbers.add(2);
		
		//오토 언방식으로 Integer가 int로 변환
		int sum = numbers.get(0) + numbers.get(1);
		System.out.println("합계 :" + sum);
		
		
	}

}
