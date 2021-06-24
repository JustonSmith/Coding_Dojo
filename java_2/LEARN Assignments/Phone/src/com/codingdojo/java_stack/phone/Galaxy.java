package com.codingdojo.java_stack.phone;

public class Galaxy extends Phone implements Ringable {
    public Galaxy(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
        super(versionNumber, batteryPercentage, carrier, ringTone);
    }
    @Override
    public String ring() {
        String ringer = getRingTone();
        		return ringer;
    }
    @Override
    public String unlock() {
    	return "phone unlocked.";
    }
    @Override
    public void displayInfo() {
        // your code here            
    }
}


