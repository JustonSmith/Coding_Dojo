package SportStarPackage;

public class Athlete {
//	Member variables:
	 protected String firstName;
	 protected String lastName;
	 protected int stamina;
	 protected int speed;
	 protected int strength;
	 	
// Constructor
	 public Athlete(String firstNameInput, String lastNameInput) {
	 	 this.firstName = firstNameInput;
	 	 this.lastName = lastNameInput;
	 	 this.stamina = 10;
	 	 this.speed = 10;
	 	 this.strength = 10;
	 	}
	 
	 public String displayStats() {
		 String result = String.format("This Athlete's stats are: \n First Name: %s Last Name: %s Strength: %d Stamina: %d Speed: %d", this.firstName, this.lastName, this.strength, this.stamina, this.speed); 
		 
		 
		 return result;
	 }
	 	
	 	
	 
	 
	 
	 
	 
	 
	 
// Getters and Setters
	 
	 
	 public String getFirstName() {
		return firstName;
	}

	 public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	 public String getLastName() {
		return lastName;
	}

	 public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	 public int getStamina() {
		return stamina;
	}

	 public void setStamina(int stamina) {
		this.stamina = stamina;
	}

	 public int getSpeed() {
		return speed;
	}

	public void setSpeed(int speed) {
		this.speed = speed;
	}

	public int getStrength() {
		return strength;
	}

	public void setStrength(int strength) {
		this.strength = strength;
	}

		

}

