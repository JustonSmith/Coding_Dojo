package com.codingdojo.javaBeltExam.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.javaBeltExam.models.Idea;
import com.codingdojo.javaBeltExam.repositories.IdeaRepository;

@Service
public class IdeaService {

	@Autowired
	private IdeaRepository ideaRepo;
	
	public Idea createIdea(Idea ideas) {
		return ideaRepo.save(ideas);
	
	}
	
	public List<Idea> findAllIdeas() {
		return ideaRepo.findAll();
	}
	
	public Idea findIdeaById(Long id) {
		Optional<Idea> u = ideaRepo.findById(id);
		
		if (u.isPresent()) {
			return u.get();
		} else {
				return null;
		}
	
	}
}