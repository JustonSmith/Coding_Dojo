package com.codingdojo.java.zookeeper2;

public class Bat {
	public class Bat extends Mammal {
		
		public Bat() {
		this.energyLevel = 500;
		}
		public void fly() {
			energyLevel -= 50;
			System.out.println("Chirp! Chatter! Whoosh! Using ecolocation, the giant bat takes flight.");
			displayEnergy();
		}
		public void eatHumans() {
			energyLevel += 25;
			System.out.println("Cruuuuunch. Human bones are brittle. The giant bat gains energy.");
			displayEnergy();
		}
		public void attackTown() {
			energyLevel -= 100;
			System.out.println("Whoosh! Smash! Crash! Explosion! The giant bat attacks the town.  Its the worst giant bat attack in town record. Hundreds die. Thousands more are injured.");
		}
		
	}
}
