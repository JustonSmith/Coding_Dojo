package com.codingdojo.java_stack.routing.controllers;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
	
@RestController
public class DojoController {
	
	@RequestMapping("{location}")
	public String dojo(@PathVariable( "location") String location) {
		if(location.equals("dojo")) {
			return "The dojo is awesome.";
		}
		
		if(location.equals("burbank-dojo")) {
			return "Burbank Dojo is located in Southern California.";
		}
		
		if(location.equals("san-jose")) {
			return "San Jose dojo is the headquarters.";
		}
		return "";
	}
}
