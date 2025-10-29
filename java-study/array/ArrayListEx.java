package array;

import java.util.ArrayList;
import java.util.Arrays;

public class ArrayListEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ArrayList<String> list = new ArrayList<>();
		list.add("Amazon");
		list.add("Google");
		System.out.println(list);
		
		ArrayList<String> list2 = new ArrayList<>();
		list2.add("Apple");
		list2.add("Samsung");
		list.addAll(list2);
		System.out.println(list);
	
		// Size
		System.out.println(list.size());
	
		// contains(params) : ArrayList가 params를 포함하고 있는지 여부
		System.out.println(list.contains("Hyundai"));
	
		// get(index)
		System.out.println(list.get(1));
		
		// set(index, element): 특정한 위치에 있는 값을 교체
		System.out.println(list.set(2, "hyundai"));
		System.out.println(list);
		
		// indexof (params) : params와 같은 첫 번째 요소의 index 리턴, 없으면 -1 리턴
		System.out.println(list.indexOf("Google"));
		
		// isEmpty : ArrayList 값이 비어 있는지 없는 지 확인
		System.out.println(Arrays.asList().isEmpty());
		
		// remove (index) : index값 지우기
		list.remove(3);
		System.out.println(list);
		
		// clear(ArrayList) : ArrayList index값을 모두 제거
		ArrayList<Integer> clearList = new ArrayList<>(Arrays.asList(1,2,3,4));
		clearList.clear();
		System.out.println(clearList.isEmpty());
		
	}
}
