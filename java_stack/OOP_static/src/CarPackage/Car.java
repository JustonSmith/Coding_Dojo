package CarPackage;
import java.util.Random;

public class Car {
	private int mileage;
	public int getMileage() {
		return mileage;
	}

	public void setMileage(int mileage) {
		this.mileage = mileage;
	}

	public String getLicensePlateNum() {
		return licensePlateNum;
	}

	public void setLicensePlateNum(String licensePlateNum) {
		this.licensePlateNum = licensePlateNum;
	}

	public double getGallonsLeft() {
		return gallonsLeft;
	}

	public void setGallonsLeft(double gallonsLeft) {
		this.gallonsLeft = gallonsLeft;
	}

	public int getMilesPerGallon() {
		return milesPerGallon;
	}

	public void setMilesPerGallon(int milesPerGallon) {
		this.milesPerGallon = milesPerGallon;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}
	
	
//	MEMBER VARIABLES
	private String licensePlateNum;
	private double gallonsLeft;
	private int milesPerGallon;
	private String model;
	
	public static int totalCarsCreated = 0;
	public static int totalMileageForAllCars = 0;
	
	
//	CONSTRUCTOR
	public Car(int mileageInput, int milesPerGallonInput, String modelInput) {
		this.mileage = mileageInput;
		this.milesPerGallon = milesPerGallonInput;
		this.model = modelInput;
		this.gallonsLeft = 35;
		this.licensePlateNum = "345363";
		
		totalCarsCreated++;
		totalMileageForAllCars += this.mileage;
	}
	
	public void drive(int numMilesDriven) {
		if(this.milesPerGallon * this.gallonsLeft > numMilesDriven) {
		this.mileage += numMilesDriven;
//		25/1 * 50/x
		
//		50/25 = x
		double numGallonsUsedUp = numMilesDriven/this.milesPerGallon;
		System.out.println(numGallonsUsedUp);
		double gallonsLeft = this.gallonsLeft - numGallonsUsedUp;
		this.setGallonsLeft(gallonsLeft);
		
		totalMileageForAllCars += numMilesDriven;
		
	}else {
		System.out.println("Better call roadside assistance");
	}
		
	}
	
		
		public String generateLicensePlateNumber() {
//			figure out how to generate a random number between 0-9.
//			do that process six times.
//			each time, add that number to an empty string.
//			results in a string of six random numbers.
			
			Random rand = new Random();
			int rand_int;
			String result = "";
			for(int i = 0; i<6; i++) {
				rand_int = rand.nextInt(10);
				result += rand_int;
				
			}
			System.out.println("License Plate: " + result);
			return "";
		}
	
}

