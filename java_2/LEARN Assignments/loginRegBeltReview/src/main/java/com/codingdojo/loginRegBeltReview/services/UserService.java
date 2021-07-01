package com.codingdojo.loginRegBeltReview.services;

import java.util.List;
import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.codingdojo.loginRegBeltReview.models.Menu;
import com.codingdojo.loginRegBeltReview.models.UserLogin;
import com.codingdojo.loginRegBeltReview.models.UserRegistration;
import com.codingdojo.loginRegBeltReview.repositories.MenuRepository;
import com.codingdojo.loginRegBeltReview.repositories.UserRepository;

@Service
public class UserService {

	@Autowired
    private UserRepository userRepo;
	
	@Autowired
	private MenuRepository menuRepo;
	    
//		REGISTRATION
	
	    public UserRegistration register(UserRegistration newUser, BindingResult result) {
	    	
//	    CUSTOM VALIDATIONS
	    	
//	    Validate that the new user object email does not already exist in the db. If it does exist, add another validation error.
	    	if(userRepo.findByEmail(newUser.getEmail()).isPresent()) {
	            result.rejectValue("email", "Unique", "This email is already in use!");
	        }
	        
//	    Validate that confirm password and password match.
	        if(!newUser.getPassword().equals(newUser.getConfirm())) {
	            result.rejectValue("confirm", "Matches", "The Confirm Password must match Password!");
	        }
	        if(result.hasErrors()) {
	            return null;
	        } else {
	            String hashed = BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
	            newUser.setPassword(hashed);
	            return userRepo.save(newUser);
	        }
	    }
	    
//	    LOGIN
	    
	    public UserRegistration login(UserLogin newLogin, BindingResult result) {
	        if(result.hasErrors()) {
	            return null;
	        }
//	        search the db for a user that has the same email as the one typed in the login form.
	        
	        Optional<UserRegistration> potentialUser = userRepo.findByEmail(newLogin.getEmail());
	        
//	        if the email is not found, "potentialUser" does not contain a user object, so create a custom validation error for "unknown email."
	        if(!potentialUser.isPresent()) {
	            result.rejectValue("email", "Unique", "Unknown email!");
	            return null;
	        }
	        
//	        at this point, the email is found and now a matching password is needed.
	        
	        UserRegistration user = potentialUser.get(); // getting the user with a matching email.
	        if(!BCrypt.checkpw(newLogin.getPassword(), user.getPassword())) { // using bCrypt to check for matching password.
	            result.rejectValue("password", "Matches", "Invalid Password!"); // password didnt match, create validation error message.
	        }
	        if(result.hasErrors()) {
	            return null;
	        } else {
//	        	at this point both email and password match, and successful login can occur.
	            return user;
	        }
	    }
	    
	    public UserRegistration findOneUser(Long id) {
	    	return this.userRepo.findById(id).orElse(null);
	    
	    }
	    
	  ///METHODS FOR THE MENU OPERATIONS
	    public List<Menu> findAllMenuItems(){
	    		return (List<Menu>)this.menuRepo.findAll();
	    }
	    
	    //create a menu item
	    public Menu createMenuItem(Menu m) {
	    		return this.menuRepo.save(m);
	    }
	    
	    //find one menu item
	    public Menu findOneMenuItem(Long id) {
	    		return this.menuRepo.findById(id).orElse(null);
	    }
	    
	    //update one menu item
	    public Menu updateOneMenuItem(Menu m) {
	    		return this.menuRepo.save(m);
	    }
	    
	    //deleete one menu item
	    public void deleteOneMenuItem(Long id) {
	    		this.menuRepo.deleteById(id);
	    }
	    
	    
	
}

