package com.codingdojo.petShelter.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.petShelter.models.Pet;
import com.codingdojo.petShelter.repositories.PetRepository;

@Service
public class PetService {
	public final PetRepository petRepo;
	
	public PetService(PetRepository petRepo) {
		this.petRepo = petRepo;
	}
	
//	find ALL pets.
	public List <Pet> allPets() {
		return (List<Pet>)this.petRepo.findAll();
	}
	
//	CREATE a pet.
	
	public Pet createPet(Pet p) {
		return this.petRepo.save(p);
	}
	
// RETRIEVE a pet.
	
//	public Pet getOnePet(Long id) {
//		Optional <Pet> optionalPet =petRepo.findById(id);
//		if(optionalPet.isPresent()) {
//			return optionalPet.get();
//		} else {
//			return null;
//		}
//	}
//	
	public Pet getOnePet(Long id) {
		return this.petRepo.findById(id).orElse(null);
	}
	
	
//	UPDATE one pet
	
	public Pet updatePet(Pet p) {
		return this.petRepo.save(p);
	}
	
//	DELETE one pet
	public void deletePet(Long id) {
		this.petRepo.deleteById(id);
	}
	
	
	
	
}
