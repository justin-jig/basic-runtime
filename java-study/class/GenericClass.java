package studyClass;

import java.util.ArrayList;


/** 일반 클래스 */
class MyCustomList {
	
	ArrayList<String> list = new ArrayList<>();
	public void addElement(String element) {
		list.add(element);
	}
	public void removeElement(String element) {
	
		list.remove(element);
	}
}

/** 제네릭클래스 */
class MyCustomList2<T> {
	ArrayList<T> list = new ArrayList<>();
	
	public void addElement (T element) {
		list.add(element);
	}
	public void removeElement (T element) {
		list.remove(element);
	}
	

}
/** 제너릭 매서드 */
class Utility {
	public <T> void printPair(T frist, T second) {
		System.out.println("(" + frist + ", " + second + ")");
	}
}


public class GenericClass {
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		/**
		 *  제네릭이란 
		 *  타입 안전성: 잘못된 타입의 객체가 저장되는 것을 컴파일 시간에 방지
		 *  형 변환 필요성 감소: 제네릭을 사용하면 명시적인 형 변환이 필요 없어짐
		 *  코드 재사용성: 일반 클래스나 메서드로 다양한 타입에 대해 동작하는 코드를 작성할 수 있음
		 */
	
		MyCustomList myCustomList = new MyCustomList();
		Utility utility = new Utility();
		utility.printPair("people", 5);
	
	}

}
