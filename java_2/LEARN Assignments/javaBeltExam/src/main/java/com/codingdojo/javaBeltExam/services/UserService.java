package com.codingdojo.javaBeltExam.services;

import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.codingdojo.javaBeltExam.models.User;
import com.codingdojo.javaBeltExam.models.UserLogin;
import com.codingdojo.javaBeltExam.repositories.ExamRepository;


@Service
public class UserService {

	@Autowired
	private ExamRepository examRepo;
	
	public User register(User newUser, BindingResult result) {
		
		if(examRepo.findByEmail(newUser.getEmail()).isPresent()) {
			result.rejectValue("email", "Unique", "This email is already in use.");
		}
		if(!newUser.getPassword().equals(newUser.getConfirm())) {
            result.rejectValue("confirm", "Matches", "The Confirm Password must match Password!");
		}
		if(result.hasErrors()) {
            return null;
        } else {
            String hashed = BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
            newUser.setPassword(hashed);
            return examRepo.save(newUser);
        }
	}
	
	public User login(UserLogin newLogin, BindingResult result) {
        if(result.hasErrors()) {
            return null;
        }
        Optional<User> potentialUser = examRepo.findByEmail(newLogin.getEmail());
        if(!potentialUser.isPresent()) {
            result.rejectValue("email", "Unique", "Unknown email!");
            return null;
        }
        User user = potentialUser.get();
        if(!BCrypt.checkpw(newLogin.getPassword(), user.getPassword())) {
        	result.rejectValue("password", "Matches", "Invalid Password!");
        }
        if(result.hasErrors()) {
            return null;
        } else {
        	return user;
        }
	}
        public User findOneUser(Long id) {
	    	return this.examRepo.findById(id).orElse(null);
	    
	    }
}
