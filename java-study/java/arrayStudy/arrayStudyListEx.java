package arrayStudy;

import java.util.arrayStudyList;
import java.util.arrayStudys;

public class arrayStudyListEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		arrayStudyList<String> list = new arrayStudyList<>();
		list.add("Amazon");
		list.add("Google");
		System.out.println(list);
		
		arrayStudyList<String> list2 = new arrayStudyList<>();
		list2.add("Apple");
		list2.add("Samsung");
		list.addAll(list2);
		System.out.println(list);
	
		// Size
		System.out.println(list.size());
	
		// contains(params) : arrayStudyList가 params를 포함하고 있는지 여부
		System.out.println(list.contains("Hyundai"));
	
		// get(index)
		System.out.println(list.get(1));
		
		// set(index, element): 특정한 위치에 있는 값을 교체
		System.out.println(list.set(2, "hyundai"));
		System.out.println(list);
		
		// indexof (params) : params와 같은 첫 번째 요소의 index 리턴, 없으면 -1 리턴
		System.out.println(list.indexOf("Google"));
		
		// isEmpty : arrayStudyList 값이 비어 있는지 없는 지 확인
		System.out.println(arrayStudys.asList().isEmpty());
		
		// remove (index) : index값 지우기
		list.remove(3);
		System.out.println(list);
		
		// clear(arrayStudyList) : arrayStudyList index값을 모두 제거
		arrayStudyList<Integer> clearList = new arrayStudyList<>(arrayStudys.asList(1,2,3,4));
		clearList.clear();
		System.out.println(clearList.isEmpty());
		
	}
}
