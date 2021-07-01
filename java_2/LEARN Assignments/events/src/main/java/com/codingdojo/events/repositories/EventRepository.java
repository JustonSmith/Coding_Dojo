package com.codingdojo.events.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.events.models.Event;
import com.codingdojo.events.models.User;

@Repository
public interface EventRepository extends CrudRepository<Event, Long> {
	
	Optional<User> findByEmail(String email);

	User save(User user);

}
