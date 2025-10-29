package practice;


class Animal{
	
	String species = ""; // 종
	String name = ""; // 이름
	int age = 0; // 나이
	
	public Animal (String species, String name, int age ) {
		this.species = species;
		this.name = name;
		this.age = age;
	}
	
	public String getinfo() {
		return "종 : " + species + "name : " + name + ", age : " + age;
	}
	
	
	public String makeSound() {
		return "동물은 소리를 낸다";
	}
	
}


class Cat extends Animal {
	
	public Cat (String name, int age) {
		
		super("고양이", name, age);
		
	}
	
	
	@Override
	public String makeSound() {
		return "야옹";
	}
	
	public String angry() {
		return "꼬리 올리기";
	}
	
}

class Dog extends Animal {
	
	public Dog (String name, int age) {
		
		super("강아지", name, age);
		
	}
	@Override
	public String makeSound() {
		return "멍멍";
	}
	
	public String angry() {
		return "꼬리 내리기";
	}
}


public class Inheritance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Cat cat = new Cat("고양쓰", 10);
		System.out.println(cat.getinfo());
		System.out.printf("울음소리 :: %s  ", cat.makeSound()).println();
		System.out.println(cat.angry());
		
		Dog dog = new Dog("강아쓰", 10);
		System.out.println(dog.getinfo());
		System.out.printf("울음소리 :: %s  ", dog.makeSound()).println();
		System.out.println(dog.angry());
		
	}

}
