package studyClass;

public class InheriStudent extends InheriPerson {

	private String major;
	
	public InheriStudent(String name, int age , String major) {
		
		// super키워드는 상위 클래스의 매서드를 호출하는데 사용
		// super() : 하위 클래스에서 오버라이드된 매서드를 호출하는데 사용
		super(name, age);
		this.major = major;
		
	}
	
	
	@Override
	// 오버라이드 => Object 부모에 있는 매서드를 재 정의
	public String toString() {
		return "Student : " + super.toString() + "major " + this.major;
	}
	

	
	
	
	
}
