package practice;

public class ClassRectangle {

	private double width = 0;
	private double height = 0;
	
	static int count = 0;

	
	public ClassRectangle ( double width) {
		
		if (width > 0 ) {
			this.width = width;
		}
		count ++;
	}
	
	public double getWidth () {
	
		return this.width;
	}


	public double getHeight () {
		
		return this.height;
	}
	
	public void setHeight (double height) {
		
		if (height > 0 ) {
			this.height = height;
		}
	}
	
	public double rectangleSize() {
		 
		return this.width * this.height;  
	}
	
	
}
