package com.codingdojo.java.ObjectMaster2;

public class Human {

//		Human attributes
		private String name = "";
		private int strength = 3;
		private int stealth = 3;
		private int intelligence = 3;
		private int health = 100;
		
//		constructors
		public Human() {
			
		}
		
		public Human(String name) {
			this.name = name;
			
		}
		
//		getters/setters
		public String getName() {
			return name;
		}
		
		public int getStrength() {
			return strength;
		}
		
		public int getStealth() {
			return stealth;
		}
		
		public int getIntelligence() {
			return intelligence;
		}
		
		public int getHealth() {
			return health;
		}
		
		public void setName(String name) {
			this.name = name;
		}
		public void setStrength(int strength) {
			this.strength = strength;
			
		}
		public void setStealth(int stealth) {
			this.stealth = stealth;
		}
		
		public void setIntelligence(int intelligence) {
			this.intelligence = intelligence;
		}
		public void setHealth(int intelligence) {
			this.health = health;
		}
		
		
//		method
		public void attack(Human human) {
			human.setHealth(human.getHealth()-strength);
			System.out.println(this.getName() + " attacks " + human.getName() + " dealing " human.getStrength() + " damage!");
		}
}
