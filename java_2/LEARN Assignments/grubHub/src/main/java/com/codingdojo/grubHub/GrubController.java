package com.codingdojo.grubHub;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GrubController {

	
	@RequestMapping("/")
	public String helloGrubHub(Model model) {
		String name = "Judge";
		int numBelts = 2;
		
		model.addAttribute("nameVariable", name );
		model.addAttribute("numBelts", numBelts);
		
		
		return "grubHome.jsp";
		
	}
	@RequestMapping("/newOrder")
	public String newOrder(Model model) {
		SimpleDateFormat formatter = new SimpleDateFormat("dd 'of the month called ' MM 'in the year of' yyyy" );
		Date date = new Date();
		System.out.println(formatter.format(date));
		model.addAttribute("dateInfo", formatter.format(date) );
		return "orderForm.jsp";
	}
	
	@RequestMapping(value= "/submitOrder", method=RequestMethod.POST) 
	public String completeOrder(@RequestParam(value = "nombre") String orderName, @RequestParam(value= "spiceLevel") String spiceLevel, @RequestParam(value="ccNum") String creditCardNum, Model model ) {
		System.out.println(orderName);
		model.addAttribute("orderName", orderName);
		model.addAttribute("spiceLevel", spiceLevel);
		model.addAttribute("ccNumber", creditCardNum);
		return "orderDetails.jsp";
		
		
	}
	
}
