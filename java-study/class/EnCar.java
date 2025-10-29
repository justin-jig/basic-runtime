package studyClass;

public class EnCar {
	
	
	int speed = 0;
	private int Pspeed = 0;
	
	int spe = 0;
	
	/** 접근제어자
	 *
	 * public : 같은 클래스 o , 같은 패키지 o , 자식 클래스 o , 전체 o
	 * protected : 같은 클래스 o, 같은 패키지 o , 자식 클래스 o , 전체 x 
	 * default : 같은 클래스 o, 같은 패키지 o , 자식 클래스 x , 전체 x
	 * private :  같은 클래스 o, 같은 패키지 x , 자식 클래스 x , 전체 x
	 *
	 */
	
	/** 생성자 */
	public EnCar (int speed) {
		this.Pspeed = speed;
	}
	
	public void start () {
		
		System.out.println("Car Start");
		System.out.println(speed);
		
	}

	public void increaseSpeed (int speed) {
		
		this.Pspeed += speed;
		
	}
	
	public void decreaseSpeed (int speed) {
		
		this.Pspeed -= speed;
		
	}
	
	// getter
	public int  getSpeed () {
		
		return Pspeed;
	}


	// setter
	public void setSpeed (int speed) {
		
		// 유효성 검사 (객체를 보호)
		if ( speed > 0 ) {
			
			this.Pspeed = speed; 
		}
	}
	

}

