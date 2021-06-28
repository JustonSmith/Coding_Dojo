package com.codingdojo.quotesDemo.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.quotesDemo.models.User;


@Repository
public interface UserRepository extends CrudRepository<User, Long> {

}
