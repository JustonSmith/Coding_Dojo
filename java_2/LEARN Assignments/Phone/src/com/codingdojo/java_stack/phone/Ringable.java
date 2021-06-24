package com.codingdojo.java_stack.phone;

public interface Ringable {
	
	public default String ring() {
		return "Ring Ring Ring!";
	}
	
	public default String unlock() {
		return "Phone Unlocked.";
	}

}
