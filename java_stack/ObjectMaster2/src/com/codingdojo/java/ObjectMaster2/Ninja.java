package com.codingdojo.java.ObjectMaster2;

public class Ninja extends Human {
	

	public Ninja() {
		this.stealth = 10;
			
	}
	public Ninja(String name) {
		this.stealth = 10;
		this.name = name;
	}
	
	public void steal(Human human) {
		human.setHealth(human.getHealth() - stealth);
		this.setHealth(this.getHealth() + stealth);
		System.out.println ("Sneak Attack!");
		System.out.println ("(" + human.getName() + "is caught off guard and takes " + stealth + " points of damage!)");
	}
	
	public void run() {
		this.setHealth(-10);
	}

}
