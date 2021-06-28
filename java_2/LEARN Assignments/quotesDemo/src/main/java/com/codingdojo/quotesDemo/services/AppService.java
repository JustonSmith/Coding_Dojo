package com.codingdojo.quotesDemo.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.quotesDemo.models.Quote;
import com.codingdojo.quotesDemo.models.User;
import com.codingdojo.quotesDemo.repositories.QuoteRepository;
import com.codingdojo.quotesDemo.repositories.UserRepository;

@Service
public class AppService {
	
	private final QuoteRepository quoteRepo;
	private final UserRepository userRepo;
	
	public AppService(QuoteRepository quoteRepo, UserRepository userRepo) {
		this.quoteRepo= quoteRepo;
		this.userRepo = userRepo;
		
	}
	
//	find ALL quotes
	
	public List<Quote> findAllQuotes() {
		return (List<Quote>) this.quoteRepo.findAll();
	}
	
//	CREATE a quote.
	
	public Quote createQuote(Quote q) {
		return this.quoteRepo.save(q);
	}

//	get ONE quote.
	
	public Quote getOneQuote (Long id) {
		return this.quoteRepo.findById(id).orElse(null);	
	}
	
//	get all USERS to populate dropdown list.
	
	public List<User> findAllUsers() {
		return (List<User>) this.userRepo.findAll();
	}
	
	
//	add user as a favorite to a quote. MANY TO MANY.
	
	public void joinQuoteToUser(Long userId, Long quoteId) {
		User u = this.userRepo.findById(userId).orElse(null);
		Quote q = this.quoteRepo.findById(quoteId).orElse(null);
		
//		update quote objects list of users who like it to add this user. MANY TO MANY.
		q.getUsersWhoLike().add(u);
		
//		save the newly update quote object to the db.
		this.quoteRepo.save(q);
	}
}
