package com.codingdojo.java_stack.displaydate;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class TimeController {
	@RequestMapping("/time")
	public String time(Model model) {
		String timePattern = "hh:mm a";
		SimpleDateFormat timeFormat = new SimpleDateFormat(timePattern);
		String date = timeFormat.format(new Date());	
		model.addAttribute("date", date);
		return "/DisplayDate/time.jsp";
	}
}
