package com.codingdojo.java_stack.calculator1;

public class Calculator {
	private Double operandOne = 0.0;
	private Double operandTwo = 0.0;
	private Double mathTotal = 0.0;
	private String operation = "";
	
	public Calculator() {
	}
	
	public Calculator(Double operandOne, Double operandTwo, String operation) {
		this.operandOne = operandOne;
		this.operandTwo = operandTwo;
		this.operation = operation;
	}
	
	public Double getOperandOne() {
		return operandOne;
	}
	
	public Double getOperandTwo() {
		return operandTwo;
	}
	
	public String getOperation() {
		return operation;
	}
	
	public Double getMathTotal() {
		return mathTotal;
	}
	
	public void setOperandOne(Double operandOne) {
		this.operandOne = operandOne;
	}
	
	public void setOperandTwo(Double operandTwo) {
		this.operandTwo = operandTwo;
	}
	
	public void setOperation (String operation) {
		this.operation = operation;
	}
	
	public void setMathTotal (Double mathTotal) {
		this.mathTotal = mathTotal;
	}
	
	public void performOperation() {
		if(getOperation().equals("+")) {
			Double total = getOperandOne() + getOperandTwo();
			setMathTotal(total);
		}
		else if(getOperation().equals(" - ")) {
			Double total = getOperandOne() - getOperandTwo();
			setMathTotal(total);
		}
	}
	public void getResults() {
		System.out.println(getMathTotal());
	}
	
}
