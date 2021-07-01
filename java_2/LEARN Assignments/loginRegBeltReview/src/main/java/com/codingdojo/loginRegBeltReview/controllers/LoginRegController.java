package com.codingdojo.loginRegBeltReview.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.loginRegBeltReview.models.Menu;
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
    
    @GetMapping("/menu/new")
    public String newMenuItem(@ModelAttribute("menu")Menu menu) {
    	return "newMenu.jsp";
    }
    
    @PostMapping("/menu/create")
    public String createMenuItem(@Valid @ModelAttribute("menu") Menu menu, BindingResult result, HttpSession session) {
    	if(result.hasErrors()) {
    		return "newMenu.jsp";
    	}else {
    		//get the logged in user using session so that we can assign the logged in user as the uploader of the menu item
    		Long idOfLoggedinUser = (Long)session.getAttribute("user_id");
    		UserRegistration loggedInUserObj = this.userServ.findOneUser(idOfLoggedinUser);
    		
    		//assign the menu's uploader to be the logged in user object
    		menu.setUploader(loggedInUserObj);
    		this.userServ.createMenuItem(menu);
    		return "redirect:/home";
    	}
    }
    
    @GetMapping("/menu/{id}/info")
    public String showMenuItem(@PathVariable("id") Long id, Model model) {
    	
    	//retrieve a menu object using this id variable
    	Menu menuObj = this.userServ.findOneMenuItem(id);
    	
    	//pass the menuObj variable to the templates 
    	model.addAttribute("menuObj", menuObj);
    	return "oneItem.jsp";
    }
    
    @GetMapping("/menu/{id}/edit")
    public String editMenuItem(@PathVariable("id")Long id, Model model) {
    	
    	//retrieve a menu object using this id variable
    	Menu menuObj = this.userServ.findOneMenuItem(id);
    	//pass this menuObj to the edit page so the form can prepopulate with this menu objects information
    	model.addAttribute("menuObj", menuObj);
    	
    	return "edit.jsp";
    	
    }
    
    @PostMapping("/menu/{id}/update")
    public String updateMenuItem(@PathVariable("id")Long id, @Valid @ModelAttribute("menuObj") Menu menu, BindingResult result ) {
    	if(result.hasErrors()) {
    		return "edit.jsp";
    	}else {
    		//get the orignial menu object from the database using the id from the PathVariable
    		Menu oGMenuObj = this.userServ.findOneMenuItem(id);
//    		System.out.println("*********");
//    		System.out.println("Original menu objects uploader is this: " + oGMenuObj.getUploader());
//    		System.out.println(menu.getUploader());
//    		System.out.println(menu.getDescription());
//    		System.out.println("*********");
    		
    		//set the menu object that came from the form's uploader to be the original uploader from the original meenu object from the db
    		menu.setUploader(oGMenuObj.getUploader());
    		this.userServ.updateOneMenuItem(menu);
    		
    		return "redirect:/home";
    	}
    }
    
    
    @GetMapping("/menu/{id}/delete")
    public String deleteMenuItem(@PathVariable("id")Long id) {
    	this.userServ.deleteOneMenuItem(id);
    	return "redirect:/home";
    }
    
    



}
