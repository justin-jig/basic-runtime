package array;

import java.util.Arrays;

public class ArrayMulti {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 이차원배열로 3년 평점 구하기 (1~4학년까지)
		double[][] score = { {3.5, 3.7}, {4.0,4.1}, {3.2,3.0}, {3.8, 3.0} };
		
		double sum = 0;
		
		for (int i = 0 ; i < score.length; i++) {
			for ( int j = 0; j< score[i].length; j++) {
				sum += score[i][j];
			}
		}
		
		int n = score.length;
		int m  = score[0].length;
		System.out.println(sum/(n*m));
		
		
		for (double arr[]: score) {
			System.out.println(Arrays.toString(arr));
		}
		
	}

}
