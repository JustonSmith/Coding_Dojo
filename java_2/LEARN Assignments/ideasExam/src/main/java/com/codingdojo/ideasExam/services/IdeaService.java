package com.codingdojo.ideasExam.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.ideasExam.models.Idea;

import com.codingdojo.ideasExam.repositories.IdeaRepository;

@Service
public class IdeaService {
	private final IdeaRepository ideaRepository;

	public IdeaService(IdeaRepository ideaRepository) {
		this.ideaRepository = ideaRepository;
	}

	public Idea createIdea(Idea idea) {
		return ideaRepository.save(idea);
	}

	public List<Idea> findAllIdeas() {
		return ideaRepository.findAll();
	}
	
	
		
	

	public Idea findIdeaById(Long id) {
		Optional<Idea> u = ideaRepository.findById(id);

		if (u.isPresent()) {
			return u.get();
		} else {
			return null;
		}
	}

}
