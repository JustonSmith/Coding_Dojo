package com.codingdojo.quotesDemo.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.quotesDemo.models.Quote;
import com.codingdojo.quotesDemo.models.User;
import com.codingdojo.quotesDemo.services.AppService;

@Controller
public class QuotesController {
	private final AppService appService;
	
	public QuotesController(AppService appService) {
		this.appService = appService;
	}
	
//	GET ALL

	@GetMapping("/")
	public String home(Model model, @ModelAttribute("quote") Quote quote) {
		this.appService.findAllQuotes();
		List<Quote> allQuotes = this.appService.findAllQuotes();
		
		model.addAttribute("allQuotes", allQuotes);
		return "quotesHome.jsp";
	}
	
//	POST NEW
	
	@PostMapping("/quotes/create")
	public String createQuote(@Valid @ModelAttribute("quote") Quote quote, BindingResult result, Model model) {
		if(result.hasErrors()) {
			List<Quote> allQuotes = this.appService.findAllQuotes();
			model.addAttribute("allQuotes", allQuotes);
			return "quotesHome.jsp";
		} else {
			this.appService.createQuote(quote);
			return "redirect:/";
		}
	}

//	GET INFO
	
	@GetMapping("/quotes/{id}/info")
	public String displayQuoteInfo(@PathVariable("id") Long id, Model model) {
		Quote q = this.appService.getOneQuote(id);
		model.addAttribute("quoteToShow", q);
//	GET ALL USERS TO POPULATE DROPDOWN
		List<User> allUsers = this.appService.findAllUsers();
		model.addAttribute("allUsers", allUsers);
		return "quotesInfo.jsp";
	}
	
	@PostMapping("/addUserToQuote/{id}")
	public String addUserToQuote(@PathVariable("id") Long quoteId) {
		return "redirect:/";
	}
	
	
	
		
}
