package com.codingdojo.java_stack.calculator1;

public class CalculatorTester {
	public static void main(String[] args) {
		Calculator testCalculator1 = new Calculator(10.50,"+",5.20);
		Calculator testCalculator2 = new Calculator(48.90, "-", 15.20);
		Calculator testCalculator3 = new Calculator(2021.32, "+", 45.82);
		testCalculator1.performOperation();
		testCalculator2.performOperation();
		testCalculator3.performOperation();
		testCalculator1.getResults();
		testCalculator2.getResults();
		testCalculator3.getResults();
		
	}
}
