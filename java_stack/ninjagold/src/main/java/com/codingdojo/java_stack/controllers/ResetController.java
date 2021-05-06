package com.codingdojo.java_stack.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ResetController {
	@RequestMapping("/reset")
	public String reset(HttpSession session) {
	session.removeAttribute("gold");
	return "redirect:/";
	}
}
