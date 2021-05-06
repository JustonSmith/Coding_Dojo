package com.codingdojo.java_stack.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SurveryController {
	@RequestMapping("/")
	public String survey() {
		return "/DojoSurvey/dojosurvey.jsp";
	}
}

