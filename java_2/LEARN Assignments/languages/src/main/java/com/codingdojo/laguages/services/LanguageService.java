package com.codingdojo.laguages.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.laguages.models.Language;
import com.codingdojo.laguages.repositories.LanguageRepository;

@Service
public class LanguageService {
	public final LanguageRepository langRepo;
	
	public LanguageService(LanguageRepository langRepo) {
		this.langRepo = langRepo;
	}
	
//	find ALL languages.
	
	public List <Language> allLanguages() {
		return (List<Language>)this.langRepo.findAll();
	}

//	CREATE a language.
	
	public Language createLanguage(Language l) {
		return this.langRepo.save(l);
	}
	
//	RETRIEVE a language.
	
	public Language getOneLanguage(Long id) {
		return this.langRepo.findById(id).orElse(null);
	}
	
//	UPDATE a language.
	
	public Language updateLanguage(Language l) {
		return this.langRepo.save(l);
	}
	
//	DELETE a language.
	
	public void deleteLanguage(Long id) {
		this.langRepo.deleteById(id);
	}
	
}
