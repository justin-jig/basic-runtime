package studyClass;

import java.util.ArrayList;

public class GenericClass3 {
	
	/** 제너릭 와일드 카드
	 * 제너릭에서 와일드 카드는 알 수 없는 타입을 의미함.
	 * ?(Unbounded Wildcard) : 어떠한 타입도 될 수 있습니다.
	 * ? extends T (Upper Bounded Wildcard): T 타입 또는 T의 서브타입을 의미
	 * ? super T (Lower Bounded Wildcard) : T 타입 또는 T의 슈퍼타입을 의미
	 */
	
	
	// Number형 제너릭 제한 와일드 카드
	public void processList(ArrayList<? extends Number> list) {
		
		for (Number num : list) {
			System.out.println(num);
		}
	}
	// 타입 파라미터
	public <T extends Number> void addToNumberList(ArrayList<T> list, T item) {
		list.add(item);
	}
	
	// ? super T
	public void processList2 (ArrayList<? super Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.add(6);
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		GenericClass3 genericClass = new GenericClass3();
		ArrayList<Integer> integerList = new ArrayList<>();
		integerList.add(1);
		integerList.add(2);
		integerList.add(3);
		
		ArrayList<Double> doubleList = new ArrayList<>();
		doubleList.add(1.1);
		doubleList.add(1.3);
		doubleList.add(3.3);
		
		// 와이드 카드 <? extends T> 은 읽기 전용으로 주로 사용
		genericClass.processList(integerList);
		genericClass.processList(doubleList);
		
		genericClass.addToNumberList(integerList, 4);
		genericClass.addToNumberList(doubleList, 4.5);
		
		
		System.out.println("----------------------");
		
		// 와일드 카드 <? super T> 는 쓰기전용으로 주로 사용
		ArrayList<Number> numbers = new ArrayList<>();
		genericClass.processList2(numbers);
		System.out.println(numbers);
		
		// 와일드 카드 주의사항
		//1. 복잡성 : 와일드카드를 가도하게 사용하게 되면 복잡성이 증가하며, 협업의 맞지 않음
		//2. 제한된작업 : '? extends T' 같은경우 새로운 요소 추가
		
		
		
	}

}
