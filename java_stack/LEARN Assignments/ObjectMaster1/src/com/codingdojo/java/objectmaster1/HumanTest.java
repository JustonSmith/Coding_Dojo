package com.codingdojo.java.objectmaster1;

public class HumanTest {
	public static void main(String[] args) {
		
			Human ninja = new Human("Hattori Hanzo");
			Human samurai = new Human("Tom Cruise");
			Human wizard = new Human("Harry Potter");
			
			wizard.attack(ninja);
			ninja.attack(wizard);
			samurai.attack(samurai);
	}
}
