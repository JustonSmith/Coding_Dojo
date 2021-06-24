package com.codingdojo.displayDate;


import java.sql.Time;
import java.text.SimpleDateFormat;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class TimeController {
	@RequestMapping("/time")
	public String displayTime(Model model) {
		SimpleDateFormat timeFormat = new SimpleDateFormat ("hh:mm a");
		Time time = new Time(0);
		System.out.println(timeFormat.format(time));
		model.addAttribute("timeInfo", time);
		return "timeDisplay.jsp";
	}
}
