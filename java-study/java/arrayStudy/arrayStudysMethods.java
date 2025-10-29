package arrayStudy;

import java.util.arrayStudys;

public class arrayStudysMethods {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] arr = { 1,2,3,4,5 };
		int[] newArr = arrayStudys.copyOf(arr, 4);
		System.out.printf("배열 :: %s", arrayStudys.toString(newArr)).println();
	
		//copyOf: 배열 전체를 복사해 복사할 길이 만큼 지정하여 복사한 새로운 배열로 반환
		int [] newArr1 = arrayStudys.copyOf(arr, 3);
		System.out.printf("copyof %s",arrayStudys.toString(newArr1)).println();

		
		//copyOfRange : 시작 인덱스부터 종료 인덱스 전까지의 부분을 복사한 새 배열을 반환
		int [] newArr2 = arrayStudys.copyOfRange(arr, 0, 4);
		System.out.printf("copyOfRange :: %s",arrayStudys.toString(newArr2)).println();
		
		//fill : 배열의 모든 요소를 주어진 값으로 채용
		arrayStudys.fill(arr, 10);
		System.out.printf("fill : %s ", arrayStudys.toString(arr)).println();;
		
		int [] arr2 = new int [5];
		arr[0] = 1;
		arr[1] = 2;
		arr[2] = 3;
		arrayStudys.fill(arr2,3, arr2.length, 100);
		System.out.printf("fill : %s ", arrayStudys.toString(arr)).println();

		// sort: 배열을 오름차순으로 정렬
		int[] arr3 = {3,2,4,5,1};
		arrayStudys.sort(arr3);
		System.out.printf("sort 배열 %s", arrayStudys.toString(arr3)).println();
		
		// arr4 배열 뒤집기
		int[] arr4 = {3,2,4,5,1};
		int[] reverseArrr = new int [5];
		//		for (int i=0; i< arr3.length; i++) {
		//			int temp = arr4[i];
		//			arr4[i] = arr4[arr.length -1 -i];
		//		}
		
		for (int i = arr4.length -1, j=0; i >=0; i--, j++) {
			
			reverseArrr[j] = arr4[i];
		}
		
		System.out.printf("배열 뒤집기 before:: %s ", arrayStudys.toString(arr4)).println();
		System.out.printf("배열 뒤집기 after:: %s ", arrayStudys.toString(reverseArrr)).println();

		// equals( arr1, arr2 ) : 두 배열의 각각의 요소 값이 동일한지 비교하여 true/false 반환
		int [] arr5 = {1,2,3,4,5};
		System.out.printf("equqls ::: %b", arrayStudys.equals(arr3, arr5)).println();
		
		
		//  deepEquals ( arr1, arr2 ) : 단일 차원 또는 다차원 배열인 두 배열이 같은지 비교하여 true/false 반환
		int [][] arrs1 = {{1,2},{1,3}};
		int [][] arrs2 = {{1,2},{1,2}};
		System.out.printf("deepEquals ::: %b", arrayStudys.deepEquals(arrs1, arrs2)).println();

		
		// binarySearch( arr, idx ): 배열의 특정 인덱스 요소값을 이진 검색 알고리즘을 사용하여 검색한 후, 해당 위치 반환
		int index = arrayStudys.binarySearch(arr3, 5);
		System.out.printf("index :: %s", arrayStudys.toString(arr3)).println();
		System.out.printf("index :: %d", index).println();
		

		
		
	}

}
