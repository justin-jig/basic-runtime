package practice;


abstract class Student {
	String name = "";
	String school = "";
	int age = 0;
	int schoolBno;
	public Student(String name, String school, int age, int schoolBno) {
		this.name = name;
		this.school = school;
		this.age = age;
		this.schoolBno = schoolBno;
	}
	abstract public void todo();
	
}

class Kim extends Student {
	
	public Kim(String name, String school, int age, int schoolBno) {
		
		super(name, school, age, schoolBno);
	}
	
	public void info (){
		System.out.println ("name :: "+ super.name + ", school :: "+ super.school 
							+ ", age ::  " + super.age + ", schoolBno :: " + super.schoolBno);
	}
	
	public void todo() {
		System.out.println("점심은 김가네 피자");
	}
}


class Baek extends Student {
	
	
	public Baek(String name, String school, int age, int schoolBno) {
		
		super(name, school, age, schoolBno);
	}
	public void info (){
		System.out.println ("name :: "+ super.name + ", school :: "+ super.school 
							+ ", age ::  " + super.age + ", schoolBno :: " + super.schoolBno);
	}
	public void todo() {
		System.out.println("점심은 백종원 피자");
	}
}


public class Abstract {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Kim kim = new Kim("김철수", "고려대학교", 20, 20234545);
		Baek baek = new Baek("이영미", "연세대학교", 20, 20234548);
		kim.info();
		kim.todo();
		
		baek.info();
		baek.todo();
	}
}
