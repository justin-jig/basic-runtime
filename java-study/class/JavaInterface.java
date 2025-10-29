package studyClass;


/** 인터페이스 
 * 1. 추상화 : 메서드를 선언하며 상속받은 클래스에서 사용하게함.
 * 2. 다중 상속 : 하나의 인터페이스는 여러 인터페이스를 구현할 수 있음.
 * 하나의 인터페이스를 통해 여러 클래스에서 공통의 동작을 정의 할 수 있고 각 클래스는 그동작을 자신의
 * 방식대로 구현 할 수 있기 때문에 인터페이스를 구현함.
 * 
 * */
interface GameConsole {
	
	void up();
	void down();
	void right();
	void left();
}


class LoLGame implements GameConsole{
	
	@Override
	public void up() {
		
		System.out.println("위로 이동");
	}
	
	@Override
	public void down() {
		
		System.out.println("아래로 이동");
	}
	@Override
	public void right() {
		
		System.out.println("오른쪽으로 이동");
	}
	@Override
	public void left() {
		
		System.out.println("왼쪽으로 이동");
	}
	
}
class DiabloGame implements GameConsole {
	
	@Override
	public void up() {
		
		System.out.println("위로 이동");
	}
	
	@Override
	public void down() {
		
		System.out.println("아래로 이동");
	}
	@Override
	public void right() {
		
		System.out.println("오른쪽으로 이동");
	}
	@Override
	public void left() {
		
		System.out.println("왼쪽으로 이동");
	}
}
/* ---------------------------------------------------------------------------*/


public class JavaInterface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		LoLGame lolgame= new LoLGame();
		lolgame.up();
		lolgame.down();
		lolgame.right();
		lolgame.left();
	
	}

}
