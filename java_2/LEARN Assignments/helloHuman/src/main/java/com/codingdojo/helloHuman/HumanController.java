package com.codingdojo.helloHuman;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HumanController {

	@RequestMapping("/name")
	public String helloHuman(@RequestParam(value="name", required= false) String searchQuery) {
		System.out.println("~~~~~~~~~~~~~~~~~");
		System.out.println(searchQuery);
		System.out.println("~~~~~~~~~~~~~~~~~");
		if(searchQuery == null) {
			return "Hello Human.";
		}else {
			;
			return "Hello" + searchQuery;
		}	
	}
	
	@RequestMapping("/name/{nameInput}")
	public String displayName(@PathVariable("nameInput") String nameOfHuman) {
		return "Sup " + nameOfHuman;
	}
	
}
