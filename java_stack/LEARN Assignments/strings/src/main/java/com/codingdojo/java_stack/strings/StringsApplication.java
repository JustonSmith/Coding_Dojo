package com.codingdojo.java_stack.strings;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class StringsApplication {

	public static void main(String[] args) {
		SpringApplication.run(StringsApplication.class, args);
	}
	
	@RequestMapping("/")
	public String niceMessage() {
		return "Hello friend! What a wonderful day!"; 
	}
	
	@RequestMapping("/random")
	public String randomMessage() {
		return "At first I was afraid, I was petrified. Thinking I could never figure out Spring install guide.";
	}
	

}
