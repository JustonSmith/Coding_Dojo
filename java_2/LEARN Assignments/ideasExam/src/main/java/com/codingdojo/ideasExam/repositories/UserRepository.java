package com.codingdojo.ideasExam.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.ideasExam.models.User;

@Repository
public interface UserRepository extends CrudRepository<User, Long> {
	User findByEmail(String email);

}

