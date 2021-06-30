package com.codingdojo.loginRegBeltReview.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.loginRegBeltReview.models.UserRegistration;

@Repository
public interface UserRepository extends CrudRepository<UserRegistration, Long> {

//	check 'keywords inside method names' table for more options.
	Optional<UserRegistration> findByEmail(String email);
}
