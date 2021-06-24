package com.codingdojo.displayDate;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class DateController {

	@RequestMapping("/date")
	public String displayDate(Model model) {
		SimpleDateFormat formatter = new SimpleDateFormat("dd 'of the month called ' MM 'in the year of' yyyy");
		Date date = new Date();
		System.out.println(formatter.format(date));
		model.addAttribute("dateInfo", formatter.format(date) );
		return "dateDisplay.jsp";
	}
	
}
