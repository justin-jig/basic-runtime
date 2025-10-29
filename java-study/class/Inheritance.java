package studyClass;

/** 상속 */
public class Inheritance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		InheriPerson person = new InheriPerson("홍길동", 30);
		
		System.out.println(person.toString());
		
		
		InheriStudent student = new InheriStudent("이몽룡", 32, "컴퓨터공학");
		System.out.println(student.toString());

		
		// 하위클래스에 부모 클래스 매서드 사용

		System.out.println(student.getName());
		System.out.println(student.getAge());
		
	}

}
