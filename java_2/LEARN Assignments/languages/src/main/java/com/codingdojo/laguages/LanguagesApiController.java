package com.codingdojo.laguages;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.codingdojo.laguages.models.Language;
import com.codingdojo.laguages.services.LanguageService;

@RestController
public class LanguagesApiController {
	private final LanguageService languageService;
	
	public LanguagesApiController(LanguageService languageService) {
		this.languageService= languageService;
	}
	
	@RequestMapping("/api/languages")
	public List<Language> index () {
		return this.languageService.allLanguages();
	}
	
	@PostMapping("api/languages/create")
	public Language create(@RequestParam(value="langName") String langName, @RequestParam(value="creator") 			String creator, @RequestParam(value= "version") Integer version) {
	
		Language l = new Language(langName, creator, version);
		return this.languageService.createLanguage(l);
	}
	
	@GetMapping("api/language/{id}")
	public Language getOneLanguage(@PathVariable("id") Long id) {
		return this.languageService.getOneLanguage(id);
	}
	
	
	
}
	
