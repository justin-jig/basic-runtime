package studyClass;


/** 다형성 
 * 하나의 인터페이스나 클래스를 여러가지 방식으로 동작하게 하는 것
 * 
 * 일반 클래스를 사용한 다형성
 * 추상 클래스를 사용한 다형성
 * 인터페이스를 사용한 다형성
 * 
 * */

// 1. 일반 클래스를 사용한 다형성

class Animal {
	public void sound() {
		System.out.println("동물은 소리를 냅니다.");
	}
}

class Dog extends Animal {
	
	@Override 
	public void sound () {
		
		System.out.println("멍멍");
	}
}
class Cat extends Animal {
	
	@Override 
	public void sound () {
		
		System.out.println("야옹");
	}
}

//2. 추상 클래스를 사용한 다형성
abstract class Shape {
	abstract double area();
}

class Circle extends Shape {
	
	private double radius;
	
	public Circle(double r) {
	
			this.radius = r;
	}

	@Override
	double area() {
		// TODO Auto-generated method stub
		return Math.PI * radius * radius;
	}
}

class Rectangle extends Shape {

	private double width;
	private double height;
	
	
	public Rectangle (double w, double h) {
		this.width = w;
		this.height = h;
		
	}
	
	
	@Override
	double area() {
		// TODO Auto-generated method stub
		return width* height;
	}
	
}
// 인터페이스를 사용한 다형성
interface Flyable {
	void fly();
}

class Bird implements Flyable {

	@Override
	public void fly() {
		// TODO Auto-generated method stub
		System.out.println("새가 난다");
	}
}

class AirPlane implements Flyable {

	@Override
	public void fly() {
		// TODO Auto-generated method stub
		System.out.println("비행기가 날아간다.");
	}
}


public class Polymorphism {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/** 다형성을 활용하여 Animal 타입의 참조 변수로 Dog와 Cat 객체를 참조 */
		// Dog dog = new Dog();
		// Cat cat = new Cat();
		Animal dog2 = new Dog();
		Animal cat2 = new Cat();
		
		dog2.sound();
		cat2.sound();
		
		
		Shape s1 = new Circle(3.3);
		Shape s2 = new Rectangle(3, 6.1);
		
		System.out.printf("원으 넓이 :: %.1f",s1.area()).println();
		System.out.printf("사각형 의 넓이 :: %.1f ",s2.area()).println();
		
		
		Shape[] s3 = { new Circle (3.4), new Rectangle(3, 6.1)};
		
		for (Shape s: s3) {
			System.out.printf("넓이 :: %.1f",s.area()).println();
		}
		
		/** instanceof 
		 * 객체가 특정 클래스나 인터페이스의 인스턴스 인지 확인하는 연사자
		 * 
		 * */
		
		
		Flyable f1 = new Bird();
		Flyable f2 = new AirPlane();
		f1.fly();
		f2.fly();
		
	}

}
