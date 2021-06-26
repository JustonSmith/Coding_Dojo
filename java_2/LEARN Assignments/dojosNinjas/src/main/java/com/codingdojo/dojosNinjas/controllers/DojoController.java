package com.codingdojo.dojosNinjas.controllers;



import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.dojosNinjas.models.Dojo;
import com.codingdojo.dojosNinjas.services.AppService;

@Controller
public class DojoController {

	private final AppService appService;
	
	public DojoController(AppService appService) {
		this.appService = appService;
	}
	
	
	@GetMapping("/")
	public String welconeToDojo(Model model, @ModelAttribute("dojo") Dojo dojo) {
		List<Dojo> allDojos = this.appService.findAllDojos();
		model.addAttribute("allDojos", allDojos);
		return "index.jsp";
	}
	
	@PostMapping("/dojos/create")
	public String createNewDojo(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		} else {
			this.appService.createDojo(dojo);
			return "redirect:/";
		}
	}
}
