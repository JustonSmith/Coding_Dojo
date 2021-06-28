package com.codingdojo.productsCategories.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.productsCategories.models.Category;
import com.codingdojo.productsCategories.models.Product;
import com.codingdojo.productsCategories.services.AppService;

@Controller
public class ProductsController {
	private final AppService appService;
	
	public ProductsController(AppService appService) {
		this.appService = appService;
	}
	
	@GetMapping("/")
	public String home(Model model, @ModelAttribute("product") Product product) {
		this.appService.findAllProducts();
		List<Product> allProducts = this.appService.findAllProducts();
		
		model.addAttribute("allProducts", allProducts);
		return "productsHome.jsp";
	}
	
	@PostMapping("/products/create")
	public String createQuote(@Valid @ModelAttribute("quote") Product product, BindingResult result, Model model) {
		if(result.hasErrors()) {
			List<Product> allQuotes = this.appService.findAllProducts();
			model.addAttribute("allQuotes", allQuotes);
			return "productsHome.jsp";
		} else {
			this.appService.createProduct(product);
			return "redirect:/";
		}	
	}
	
	@GetMapping("/products/{id}/info")
	public String displayProductInfo(@PathVariable("id") Long id, Model model) {
		Product p = this.appService.getOneProduct(id);
		model.addAttribute("productToShow", p);
		List<Category> allCategories = this.appService.findAllCategories();
		model.addAttribute("allCategories", allCategories);
		return "productsInfo.jsp";
		
	}
	
	@PostMapping("addCategory/${productToShow.id}")
	public String addUserToQuote(@PathVariable("id") Long productId) {
		return "redirect:/";
	}
	
	
}
