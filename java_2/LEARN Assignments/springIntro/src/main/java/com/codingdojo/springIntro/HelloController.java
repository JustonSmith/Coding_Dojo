package com.codingdojo.springIntro;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/greeting")
public class HelloController {
//	route for localhost:8080/greeting
	@RequestMapping ("/")
	public String sayHello () {
		return "Hello everybody. Welcome to spring!";
	}
	
//	route for localhost:8080/greeting/summer
	@RequestMapping("/summer")
	public String welcomeToSummer() {
		return "Summertime y'all. We still coding in spring tho.";
	}
	
//	route for localhost:8080/greeting/fall
	@RequestMapping(value= "/fall", method= RequestMethod.POST)
	public String welcomeToFall( ) {
		return "Welcome to the fall... But we rise when we follow the 20 min rule and put work in.";
	}
}
