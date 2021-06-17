package com.codingdojo.java.zookeeper2;

public class Mammal {
	public int energyLevel = 500;
	
	public int displayEnergy() {
		System.out.println("Energy Level: " + energyLevel);
		return energyLevel;
	}
}
