package com.codingdojo.loginRegBeltReview.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.loginRegBeltReview.models.UserLogin;
import com.codingdojo.loginRegBeltReview.models.UserRegistration;
import com.codingdojo.loginRegBeltReview.services.UserService;

@Controller
public class LoginRegController {
	
	@Autowired
    private UserService userServ;
    
    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("newUser", new UserRegistration());
        model.addAttribute("newLogin", new UserLogin());
        return "index.jsp";
    }
    
    @PostMapping("/register")
    public String register(@Valid @ModelAttribute("newUser") UserRegistration newUser, 
            BindingResult result, Model model, HttpSession session) {
    	
        userServ.register(newUser, result);
        if(result.hasErrors()) {
            model.addAttribute("newLogin", new UserLogin());
            return "index.jsp";
        }

//		Keep track of users ID in session.         
        session.setAttribute("user_id", newUser.getId());
        return "redirect:/home";
    }
    
    @PostMapping("/login")
    public String login(@Valid @ModelAttribute("newLogin") UserLogin newLogin, 
            BindingResult result, Model model, HttpSession session) {
    	
        UserRegistration user = userServ.login(newLogin, result);
        if(result.hasErrors()) {
            model.addAttribute("newUser", new UserRegistration());
            return "index.jsp";
        }
        
//        if there are no errors, and the form info is all valid, session is used to store the users info to log them into the dashboard.
        session.setAttribute("user_id", user.getId());
        return "redirect:/home";
    }
    
    @GetMapping("/home")
    public String home(HttpSession session, Model model) {
    		System.out.println("************");
    		System.out.println(session.getAttribute("user_id"));
    		System.out.println("************");
    		if(session.getAttribute("user_id") == null) {
    			return "redirect:/";
    		}
    	
//    	use session to retrieve the id of the logged in user or newly registered user.
    	
    	Long loggedInId = (Long)session.getAttribute("user_id");
    	
//    	use the retrieved id to find a user from the database who has that id, so we can send that user's information to the template. (JSP)
    	
    	UserRegistration loggedInUserObj = this.userServ.findOneUser(loggedInId);
    	model.addAttribute("loggedInUser", loggedInUserObj);
    	return "dashboard.jsp";
    	
    }
    
    @GetMapping("/logout")
    public String logout(HttpSession session) {
    	session.removeAttribute("user_id");
    	return "redirect:/";
    	
    }

}
