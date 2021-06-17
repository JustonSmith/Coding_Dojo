package SportStarPackage;

public class BasketballPlayer extends Athlete { // 'extends' keyword allows for inheritance from Athlete class.
	// member variable unique to BasketballPlayer class.
	private int shootingSkillLevel;
	
	//constructor
	public BasketballPlayer(String firstNameInput, String lastNameInput, int shootingLevelInput) {
	//'super' is used to say, "do whatever you are doing for the constructor of the parent class"
		super(firstNameInput, lastNameInput);
		this.shootingSkillLevel = shootingLevelInput;
		this.stamina = 25;
	}
	
	public String displayStats() {
		 String result = String.format("This Basketball Player's stats are: \n First Name: %s Last Name: %s Strength: %d Stamina: %d Speed: %d, Shooting Skill: %d", this.firstName, this.lastName, this.strength, this.stamina, this.speed, this.shootingSkillLevel);
		 
		 return result;
	}
	
	//methods only a basketball player can do.
	public void shootBall() {
		this.stamina -= 5;
		if (this.shootingSkillLevel > 50) {
			System.out.println ("BAAAAANG!");
		}else {
			System.out.println("Brick City y'all.");
		}
	}
	
	public int getShootingSkillLevel() {
		return shootingSkillLevel;
	}
	public void setShootingSkillLevel(int shootingSkillLevel) {
		this.shootingSkillLevel = shootingSkillLevel;
	}

}
