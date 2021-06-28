package com.codingdojo.quotesDemo.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.quotesDemo.models.Quote;


@Repository
public interface QuoteRepository extends CrudRepository<Quote, Long> {

}
