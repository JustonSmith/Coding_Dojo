package SportStarPackage;

public class Swimmer extends Athlete{
	private int lungCapacity;
	
	public Swimmer (String firstNameInput, String lastNameInput, int lungCapacityInput) {
		super(firstNameInput, lastNameInput);
		this.lungCapacity = lungCapacityInput;
	}
	
	public String displayStats() {
		 String result = String.format("This Swimmer's stats are: \n First Name: %s Last Name: %s Strength: %d Stamina: %d Speed: %d, Lung Capacity: %d", this.firstName, this.lastName, this.strength, this.stamina, this.speed, this.lungCapacity);
		 
		 return result;
	}
	
	public void swim() {
		System.out.println("Swimming in salt water tho");
		this.stamina -=5;
		this.lungCapacity += 2;
	}
}
