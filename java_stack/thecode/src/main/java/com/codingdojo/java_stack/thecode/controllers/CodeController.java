package com.codingdojo.java_stack.thecode.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class CodeController {
	@RequestMapping("/")
	public String index() {
		return "/TheCode/index.jsp";
	}
}
