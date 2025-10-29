package studyBasic;

public class Loop {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		forLoop();
		whileLoop();
		
	}
	
	public static void forLoop() {
		for (int i = 0; i < 10; i++) {
			System.out.print(i);
		}
		
	}
	
	public static void whileLoop() {
		int i = 0;
		while ( i < 10 ) {
			System.out.print(i);
			i++;
		}	
	}
}
