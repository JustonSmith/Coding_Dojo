package SportStarPackage;

public class AthleteTest {

	public static void main(String[] args) {
		Athlete athlete1 = new Athlete("Rodger", "Federer");
		System.out.println(athlete1.getFirstName());
		System.out.println(athlete1.getSpeed());
		System.out.println(athlete1.displayStats());
		
		BasketballPlayer stephCurry = new BasketballPlayer("Steph", "Curry", 100);
		
		BasketballPlayer shaq = new BasketballPlayer("Shaquille", "O'neal", 15);
		
		System.out.println(stephCurry.displayStats());
		System.out.println(shaq.displayStats());
		stephCurry.shootBall();
		shaq.shootBall();
		System.out.println(stephCurry.displayStats());
		System.out.println(shaq.displayStats());
		
		Swimmer phelps = new Swimmer("Michael", "Phelps", 100);
		System.out.println(phelps.displayStats());
		
		Swimmer someoneWhoDidNotWinGoldForUSA = new Swimmer("Somebody", "Idk", 75);
		System.out.println(someoneWhoDidNotWinGoldForUSA.displayStats());
		someoneWhoDidNotWinGoldForUSA.swim ();
		System.out.println(someoneWhoDidNotWinGoldForUSA.displayStats());
	}

}
