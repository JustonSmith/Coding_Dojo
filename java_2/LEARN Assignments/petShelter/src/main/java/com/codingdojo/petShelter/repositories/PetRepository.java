package com.codingdojo.petShelter.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.petShelter.models.Pet;

@Repository
public interface PetRepository extends CrudRepository<Pet, Long> {
	List<Pet> findAll();

}
