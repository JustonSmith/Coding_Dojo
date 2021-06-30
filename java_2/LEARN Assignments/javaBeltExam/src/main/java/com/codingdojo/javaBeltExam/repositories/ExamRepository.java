package com.codingdojo.javaBeltExam.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

import com.codingdojo.javaBeltExam.models.User;

public interface ExamRepository extends CrudRepository<User, Long> {

	Optional<User> findByEmail(String email);
	
}
