package com.codingdojo.javaBeltExam.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.javaBeltExam.models.User;
import com.codingdojo.javaBeltExam.models.UserLogin;
import com.codingdojo.javaBeltExam.services.UserService;

@Controller
public class LoginRegistrationController {

	@Autowired
	private UserService userServ;
	
	@GetMapping("/")
	public String index(Model model) {
		model.addAttribute("newUser", new User());
		model.addAttribute("newLogin", new UserLogin());
		return "index.jsp";
	}
	
	@PostMapping("/register")
    public String register(@Valid @ModelAttribute("newUser") User newUser, 
            BindingResult result, Model model, HttpSession session) {
    		
		userServ.register(newUser, result);
        if(result.hasErrors()) {
            model.addAttribute("newLogin", new UserLogin());
            return "index.jsp";
        }
        	
        session.setAttribute("user_id",newUser.getId());
		return "redirect:/home";
		
    }
        
        
//    @GetMapping("/dashboard")
//    public String dashboard(HttpSession session, Model model) {
//    	System.out.println("************");
//    	System.out.println(session.getAttribute("user_id"));
//    	System.out.println("************");
//    	if(session.getAttribute("user-id") == null) {
//    		return "redirect:/";
//    	} else {
//    	
//    	Long loggedInId = (Long)session.getAttribute("user_id");
//    	User loggedInUserObj = this.userServ.findOneUser(loggedInId);
//    	model.addAttribute("loggedInUser", loggedInUserObj);
//    		return "dashboard.jsp";
//    	
    
		
	
	@PostMapping("/login")
    public String login(@Valid @ModelAttribute("newLogin") UserLogin newLogin, 
            BindingResult result, Model model, HttpSession session) {
    	
        User user = userServ.login(newLogin, result);
        if(result.hasErrors()) {
            model.addAttribute("newUser", new User());
            return "index.jsp";
        }
   
        session.setAttribute("user_id", user.getId());
        return "redirect:/home";
        
    }
	
	@GetMapping("/home")
    public String home(HttpSession session, Model model) {
    		System.out.println("************");
    		System.out.println(session.getAttribute("user_id"));
    		System.out.println("************");
    		if(session.getAttribute("user_id") == null) {
    			return "dashboard.jsp";
    		}
    	
    	Long loggedInId = (Long)session.getAttribute("user_id");    	
    	User loggedInUserObj = this.userServ.findOneUser(loggedInId);
    	model.addAttribute("loggedInUser", loggedInUserObj);
    	return "dashboard.jsp";
    	
    }
    
	
	@GetMapping("/logout")
    public String logout(HttpSession session) {
    	session.removeAttribute("user_id");
    	return "redirect:/";
	}
	
}

	

