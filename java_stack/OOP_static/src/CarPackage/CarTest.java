package CarPackage;

public class CarTest {
	
	public static void main (String[] args) { 
		Car c1 = new Car(0, 25, "BooGatti");
		System.out.println(c1.getMileage());
		System.out.println(c1.getModel());
		
		System.out.println(Car.totalCarsCreated);
		
		Car c2 = new Car(2000, 30, "Camry");
		System.out.println(c2.getMileage());
		System.out.println(c2.getModel());
		
		System.out.println(Car.totalCarsCreated);
		
		Car c3 = new Car(100000, 20, "Jeep");
		System.out.println(c3.getMileage());
		System.out.println(c3.getModel());
		
		System.out.println(Car.totalCarsCreated);
		
		Car c4 = new Car(150000, 15, "Corvette");
		System.out.println(c4.getMileage());
		System.out.println(c4.getModel());
		
		System.out.println(Car.totalCarsCreated);
		
		Car c5 = new Car(50000, 40, "Prius");
		System.out.println(c5.getMileage());
		System.out.println(c5.getModel());
		
		System.out.println(Car.totalCarsCreated);
		
		c1.drive(34);
		
		System.out.println("Total mileage for all cars: " + Car.totalMileageForAllCars);
		
		c1.generateLicensePlateNumber();
		
	}
}
