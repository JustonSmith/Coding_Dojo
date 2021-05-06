package com.codingdojo.java_stack.displaydate;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class IndexController{
	@RequestMapping("/")
	public String index() {
		return "/DisplayDate/index.jsp";
	}
}
