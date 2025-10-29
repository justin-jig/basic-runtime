package studyClass;

/** 모든 클래스는 Object를 상속 받음 */
public class InheriPerson{

	String name;
	int age;
	
	/** 접근제어자
	 *
	 * public : 같은 클래스 o , 같은 패키지 o , 자식 클래스 o , 전체 o
	 * protected : 같은 클래스 o, 같은 패키지 o , 자식 클래스 o , 전체 x 
	 * default : 같은 클래스 o, 같은 패키지 o , 자식 클래스 x , 전체 x
	 * private :  같은 클래스 o, 같은 패키지 x , 자식 클래스 x , 전체 x
	 *
	 */
	
	public InheriPerson(String name, int age) {
		this.name = name;
		this.age = age;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public int getAge() {
		return age;
	}


	public void setAge(int age) {
		this.age = age;
	}
	
	
	@Override
	// 오버라이드 => Object 부모에 있는 매서드를 재 정의
	public String toString() {
		return "Person / name : " + name + ", age : " + age;
	}
	
//	// 오버 로딩 => 
//	public String toString( int a) {
//		return "Person / name : " + name + ", age : " + age;
//	}
	
	
	
}
