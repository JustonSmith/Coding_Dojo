package com.codingdojo.dojosNinjas.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.dojosNinjas.models.Dojo;
import com.codingdojo.dojosNinjas.repositories.DojoRepository;
import com.codingdojo.dojosNinjas.repositories.NinjaRepository;

@Service
public class AppService {
	
	private final DojoRepository dojoRepo;
	
	private final NinjaRepository ninjaRepo;
	
	public AppService(DojoRepository dojoRepo, NinjaRepository ninjaRepo) {
		this.dojoRepo = dojoRepo;
		this.ninjaRepo = ninjaRepo;
	}
	
	public List<Dojo> findAllDojos() {
		return (List<Dojo>)this.dojoRepo.findAll();
	}
	
	public Dojo createDojo(Dojo d) {
		return this.dojoRepo.save(d);
	}
	
}
