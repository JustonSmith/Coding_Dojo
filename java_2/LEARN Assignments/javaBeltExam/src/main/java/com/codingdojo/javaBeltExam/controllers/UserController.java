package com.codingdojo.javaBeltExam.controllers;

import java.util.List;

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

import com.codingdojo.javaBeltExam.models.Idea;
import com.codingdojo.javaBeltExam.models.User;
import com.codingdojo.javaBeltExam.models.UserLogin;
import com.codingdojo.javaBeltExam.repositories.IdeaRepository;
import com.codingdojo.javaBeltExam.repositories.UserRepository;
import com.codingdojo.javaBeltExam.services.IdeaService;
import com.codingdojo.javaBeltExam.services.UserService;

@Controller
public class UserController {

	@Autowired
	private UserService userServ;
	
	@Autowired
	private IdeaService ideaServ;
	
	@Autowired
	private UserRepository userRepo;
	
	@Autowired
	private IdeaRepository ideaRepo;
	
	@GetMapping("/")
	public String index(Model model) {
		model.addAttribute("newUser", new User());
		model.addAttribute("newLogin", new UserLogin());
		return "loginReg.jsp";
	}
	
	@PostMapping("/registration")
    public String register(@Valid @ModelAttribute("newUser") User newUser, 
            BindingResult result, Model model, HttpSession session) {
    		
		userServ.register(newUser, result);
        if(result.hasErrors()) {
            model.addAttribute("newLogin", new UserLogin());
            return "loginReg.jsp";
        }
        	
        session.setAttribute("user_id",newUser.getId());
		return "index.jsp";
		
    }
		
	
	@PostMapping("/login")
    public String login(@Valid @ModelAttribute("newLogin") UserLogin newLogin, 
            BindingResult result, Model model, HttpSession session) {
    	
        User u = userServ.login(newLogin, result);
        if(result.hasErrors()) {
            model.addAttribute("newUser", new User());
            return "loginReg.jsp";
        }
   
        session.setAttribute("user_id", u.getId());
        return "redirect:/ideas";
        
    }
	
	@GetMapping("/ideas")
	public String home(Model model, HttpSession session) {
		List<Idea> ideas = ideaServ.findAllIdeas();
		model.addAttribute("ideas", ideas);
		User u = userServ.findOneUser((Long) session.getAttribute("userId"));
		model.addAttribute("newUser", u);
		return "index.jsp";
    	
    }
	
	@GetMapping("/ideas/new")
	public String createIdea(@ModelAttribute("ideas") Idea ideas) {
		return "newIdea.jsp";
	}
	
	@PostMapping("/ideas/new")
	public String createIdeaPost(@Valid @ModelAttribute("ideas") Idea ideas, BindingResult result, HttpSession session) {
		if (result.hasErrors()) {
			return "newIdea.jsp";
		} else {
			User u = userServ.findOneUser((Long) session.getAttribute("userId"));
			ideas.setCreator(u);
			Idea m = ideaRepo.save(ideas);
			return "redirect:/ideas";
		}
	}
	
	@GetMapping("/show/{id}")
	public String show(@PathVariable("id") Long id, Model model) {
		Idea m = ideaServ.findIdeaById(id);
		model.addAttribute("idea", m);
		return "showIdea.jsp";
	}
	
	@GetMapping("/ideas/edit/{id}")
	public String edit(@PathVariable("id") Long id, Model model) {
		Idea m = ideaServ.findIdeaById(id);
		model.addAttribute("ideas", m);
		return "editIdea.jsp";
	}
	
	@PostMapping("/ideas/edit/{id}")
	public String actuallyEdit(@PathVariable("id") Long id, @Valid @ModelAttribute("idea") Idea idea,
			BindingResult result) {
		if (result.hasErrors()) {
			return "editIdea.jsp";
		} else {
			Idea old = ideaServ.findIdeaById(id);
			idea.setCreator(old.getCreator());
			idea.setLikers(old.getLikers());
			ideaRepo.save(idea);
			return "redirect:/ideas";
		}
	}
		
	@GetMapping("/like/{id}")
	public String like(@PathVariable("id") Long id, HttpSession session) {
		User u = userServ.findOneUser((Long) session.getAttribute("userId"));
		Idea m = ideaServ.findIdeaById(id);
		m.getLikers().add(u);
		ideaRepo.save(m);
		return "redirect:/ideas";
		}

	@GetMapping("/unlike/{id}")
	public String unlike(@PathVariable("id") Long id, HttpSession session) {
		User u = userServ.findOneUser((Long) session.getAttribute("userId"));
		Idea m = ideaServ.findIdeaById(id);
		for (int i = 0; i < m.getLikers().size(); i++) {
			if (u.getId() == m.getLikers().get(i).getId()) {
				m.getLikers().remove(i);
				break;
				}
			}
			ideaRepo.save(m);
			return "redirect:/ideas";
		}
		
	@GetMapping("/delete/{id}")
	public String delete(@PathVariable("id") Long id) {
		ideaRepo.deleteById(id);
		return "redirect:/ideas";
		}
	
	@GetMapping("/logout")
    public String logout(HttpSession session) {
    	session.removeAttribute("user_id");
    	return "redirect:/";
	}
	
}

	

