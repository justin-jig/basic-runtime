package practice;


interface Playable {
	void play();
	void pause();
	void stop ();
}

class MP3Player implements Playable {

	@Override
	public void play() {
		// TODO Auto-generated method stub
		System.out.println("MP3 play");
	}

	@Override
	public void pause() {
		// TODO Auto-generated method stub
		System.out.println("MP3 pause");
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		System.out.println("MP3 stop");
	}
	
}

class DVDPlayer implements Playable {

	@Override
	public void play() {
		// TODO Auto-generated method stub
		System.out.println("DVD play");

	}

	@Override
	public void pause() {
		// TODO Auto-generated method stub
		System.out.println("DVD pause");

	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		System.out.println("DVD stop");

	}
	
}



public class Interface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		MP3Player mp3 = new MP3Player();
		DVDPlayer dvd = new DVDPlayer();
		
		mp3.play();
		mp3.pause();
		mp3.stop();
		System.out.println("------------------------");
		dvd.play();
		dvd.pause();
		dvd.stop();
		
	
		
	}

}
