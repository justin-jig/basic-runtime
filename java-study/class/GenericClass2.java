package studyClass;

class Box<T extends Number> { // Number형으로 제너릭 제한
	
	private T item;
	
	public void setItem (T item) {
		this.item = item;
	}
	
	public T getItem() {
		return item;
	}
	
}

interface Movable {
	void move();
}

class Car3 implements Movable {
	
	@Override
	public void move() {
		System.out.println("자동차 출발");
	}
}

// 재너릭 클래쓰

class Container<T extends Movable> {
	
	private T item;
	
	public Container(T item) {
		this.item = item;
	}
	public void makeItMove() {
		item.move();
	}

}



public class GenericClass2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Box<Number> nubmerBox = new Box<Number>();
		Box<Double> doubleBox = new Box<Double>();
		Box<Short> shortBox = new Box<Short>();
		
		Container<Car3> container= new Container<>(new Car3());
		
		
	}

}
